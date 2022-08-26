/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.spark.sql.sparkconnect.planner

import org.apache.spark.connect.proto
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.catalyst.{expressions, plans}
import org.apache.spark.sql.catalyst.analysis.{UnresolvedAlias, UnresolvedAttribute, UnresolvedFunction, UnresolvedRelation, UnresolvedStar}
import org.apache.spark.sql.catalyst.expressions.{Attribute, AttributeReference, Expression}
import org.apache.spark.sql.catalyst.plans.logical.{LogicalPlan, SubqueryAlias}
import org.apache.spark.sql.catalyst.plans.logical
import org.apache.spark.sql.types.{BinaryType, ByteType, DateType, DoubleType, FloatType, IntegerType, ShortType, TimestampType}

final case class InvalidPlanInput(
  private val message: String = "",
  private val cause: Throwable = None.orNull)
  extends Exception(message, cause)

case class SparkConnectPlanner(plan: proto.Relation, session: SparkSession) {

  def transform(): LogicalPlan = {
    transformRelation(plan)
  }

  // The root of the query plan is a relation and we apply the transformations to it.
  private def transformRelation(rel: proto.Relation): LogicalPlan = {
    rel.relType match {
      case proto.Relation.RelType.Read(r) => transformReadRel(r, rel.common)
      case proto.Relation.RelType.Project(r) => transformProject(r, rel.common)
      case proto.Relation.RelType.Filter(r) => transformFilter(r)
      case proto.Relation.RelType.Fetch(r) => transformFetch(r)
      case proto.Relation.RelType.Join(r) => transformJoin(r)
      case proto.Relation.RelType.Union(r) => transformUnion(r)
      case proto.Relation.RelType.Sort(r) => transformSort(r)
      case proto.Relation.RelType.Aggregate(r) => transformAggregate(r)
      case proto.Relation.RelType.Sql(r) => transformSql(r)
      case proto.Relation.RelType.LocalRelation(r) => transformLocalRelation(r)
      case proto.Relation.RelType.Empty =>
        throw new IndexOutOfBoundsException("Expected Relation to be set, but is empty.")
      case _ => throw InvalidPlanInput(s"${rel.relType} not supported.")
    }
  }

  private def transformSql(sql: proto.Sql): LogicalPlan = {
    session.sessionState.sqlParser.parsePlan(sql.query)
  }

  private def transformReadRel(
    rel: proto.Read,
    common: Option[proto.RelationCommon]): LogicalPlan = {
    val baseRelation = rel.readType match {
      case proto.Read.ReadType.NamedTable(t) =>
        val child = UnresolvedRelation(t.parts)
        if (common.nonEmpty && common.get.alias.nonEmpty) {
          SubqueryAlias(identifier = common.get.alias, child = child)
        } else {
          child
        }
      case _ => throw InvalidPlanInput()
    }
    baseRelation
  }

  private def transformLocalRelation(
    rel: proto.LocalRelation): LogicalPlan = {
    val attributes = rel.attributes.map(transformAttribute(_)).toSeq
    new org.apache.spark.sql.catalyst.plans.logical.LocalRelation(attributes)
  }

  private def transformFilter(rel: proto.Filter): LogicalPlan = {
    assert(rel.input.nonEmpty)
    val baseRel = transformRelation(rel.getInput)
    logical.Filter(condition = transformExpression(rel.getCondition), child = baseRel)
  }

  private def transformProject(
    rel: proto.Project,
    common: Option[proto.RelationCommon]): LogicalPlan = {
    val baseRel = transformRelation(rel.getInput)
    val projection = if (rel.expressions.isEmpty) {
      Seq(UnresolvedStar(Option.empty))
    } else {
      rel.expressions.map(transformExpression).map(UnresolvedAlias(_))
    }
    val project = logical.Project(projectList = projection, child = baseRel)
    if (common.nonEmpty && common.get.alias.nonEmpty) {
      logical.SubqueryAlias(identifier = common.get.alias, child = project)
    } else {
      project
    }
  }

  private def transformUnresolvedExpression(exp: proto.Expression): UnresolvedAttribute = {
    UnresolvedAttribute(exp.getUnresolvedAttribute.parts)
  }

  private def transformExpression(exp: proto.Expression): Expression = {
    exp.exprType match {
      case proto.Expression.ExprType.Literal(l) => transformLiteral(l)
      case proto.Expression.ExprType.UnresolvedAttribute(_) => transformUnresolvedExpression(exp)
      case proto.Expression.ExprType.UnresolvedFunction(f) => transformScalarFunction(f)
      case _ => throw InvalidPlanInput()
    }
  }

  private def transformAttribute(exp: proto.Expression.Attribute): Attribute = {
    AttributeReference(exp.name, IntegerType, exp.nullability)()
  }

  /**
   * Transforms the protocol buffers literal into the appropriate Catalyst literal expression.
   *
   * TODO: Missing support for Instant, BigDecimal, LocalDate, LocalTimestamp, Duration, Period.
   * @param lit
   * @return Expression
   */
  private def transformLiteral(lit: proto.Expression.Literal): Expression = {
    lit.literalType match {
      case proto.Expression.Literal.LiteralType.Boolean(b) => expressions.Literal(b)
      case proto.Expression.Literal.LiteralType.I8(v) => expressions.Literal(v, ByteType)
      case proto.Expression.Literal.LiteralType.I16(v) => expressions.Literal(v, ShortType)
      case proto.Expression.Literal.LiteralType.I32(v) => expressions.Literal(v)
      case proto.Expression.Literal.LiteralType.I64(v) => expressions.Literal(v)
      case proto.Expression.Literal.LiteralType.Fp32(v) => expressions.Literal(v, FloatType)
      case proto.Expression.Literal.LiteralType.Fp64(v) => expressions.Literal(v, DoubleType)
      case proto.Expression.Literal.LiteralType.String(v) => expressions.Literal(v)
      case proto.Expression.Literal.LiteralType.Binary(v) => expressions.Literal(v, BinaryType)
      // Microseconds since unix epoch.
      case proto.Expression.Literal.LiteralType.Timestamp(v) =>
        expressions.Literal(v, TimestampType)
      // Days since UNIX epoch.
      case proto.Expression.Literal.LiteralType.Date(v) => expressions.Literal(v, DateType)
      case _ => throw InvalidPlanInput("Unsupported Literal Type")
    }
  }

  private def transformFetch(limit: proto.Fetch): LogicalPlan = {
    logical.Limit(
      child = transformRelation(limit.getInput),
      limitExpr = expressions.Literal(limit.limit, IntegerType))
  }

  private def lookupFunction(name: String, args: Seq[Expression]): Expression = {
    UnresolvedFunction(Seq(name), args, isDistinct = false)
  }

  private def transformScalarFunction(fun: proto.Expression.UnresolvedFunction): Expression = {
    val funName = fun.parts.mkString(".")
    funName match {
      case "gt" =>
        expressions.GreaterThan(
          transformExpression(fun.arguments(0)),
          transformExpression(fun.arguments(1)))
      case "eq" =>
        expressions.EqualTo(
          transformExpression(fun.arguments(0)),
          transformExpression(fun.arguments(1)))
      case _ => lookupFunction(funName, fun.arguments.map(transformExpression))
    }
  }

  private def transformUnion(u: proto.Union): LogicalPlan = {
    assert(u.inputs.size == 2, "Union must have 2 inputs")
    val plan = logical.Union(transformRelation(u.inputs(0)), transformRelation(u.inputs(1)))

    u.unionType match {
      case proto.Union.UnionType.UNION_TYPE_DISTINCT => logical.Distinct(plan)
      case proto.Union.UnionType.UNION_TYPE_ALL => plan
      case _ =>
        throw InvalidPlanInput(s"Unsupported set operation ${u.unionType}")
    }
  }

  private def transformJoin(rel: proto.Join): LogicalPlan = {
    assert(rel.left.nonEmpty && rel.right.nonEmpty, "Both join sides must be present")
    logical.Join(
      left = transformRelation(rel.getLeft),
      right = transformRelation(rel.getRight),
      // TODO
      joinType = plans.Inner,
      condition = Some(transformExpression(rel.getOn)),
      hint = logical.JoinHint.NONE)
  }

  private def transformSort(rel: proto.Sort): LogicalPlan = {
    assert(rel.sortFields.nonEmpty, "SortFields must be present.")
    logical.Sort(
      child = transformRelation(rel.getInput),
      global = true,
      order = rel.sortFields.map(transformSortOrderExpression))
  }

  private def transformSortOrderExpression(so: proto.Sort.SortField): expressions.SortOrder = {
    expressions.SortOrder(
      child = transformUnresolvedExpression(so.getExpression),
      direction = so.direction match {
        case proto.Sort.SortDirection.SORT_DIRECTION_DESCENDING => expressions.Descending
        case _ => expressions.Ascending
      },
      nullOrdering = so.nulls match {
        case proto.Sort.SortNulls.SORT_NULLS_LAST => expressions.NullsLast
        case _ => expressions.NullsFirst
      },
      sameOrderExpressions = Seq.empty)
  }

  private def transformAggregate(rel: proto.Aggregate): LogicalPlan = {
    assert(rel.input.nonEmpty)
    assert(rel.groupingSets.size == 1, "Only one grouping set supported")

    val groupingSet = rel.groupingSets.take(1)
    val ge = groupingSet
      .flatMap(f => f.aggregateExpressions)
      .map(transformExpression)
      .map {
        case x @ UnresolvedAttribute(_) => x
        case x => UnresolvedAlias(x)
      }

    logical.Aggregate(
      child = transformRelation(rel.getInput),
      groupingExpressions = ge,
      aggregateExpressions = rel.measures.map(transformAggregateExpression) ++ ge)
  }

  private def transformAggregateExpression(
    exp: proto.Aggregate.Measure): expressions.NamedExpression = {
    val fun = exp.getFunction.name
    UnresolvedAlias(
      UnresolvedFunction(
        name = fun,
        arguments = exp.getFunction.arguments.map(transformExpression),
        isDistinct = false))
  }

}
