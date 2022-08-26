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
package org.apache.spark.sql.connect.planner

import org.apache.spark.SparkFunSuite
import org.apache.spark.connect.proto
import org.apache.spark.sql.catalyst.expressions.AttributeReference
import org.apache.spark.sql.catalyst.plans.PlanTest
import org.apache.spark.sql.catalyst.plans.logical.{LocalRelation, LogicalPlan}
import org.apache.spark.sql.sparkconnect.plans._
import org.apache.spark.sql.test.SharedSparkSession
import org.apache.spark.sql.types.IntegerType

class SparkConnectProtocolSuite extends SparkFunSuite
  with SharedSparkSession with SparkConnectPlanTest with PlanTest {

  val testRelation = LocalRelation(AttributeReference("a", IntegerType, nullable = true)())
  val connectTestRelation =
    proto.Relation().withLocalRelation(
      proto.LocalRelation().addAttributes(
        proto.Expression.Attribute().withName("a").withNullability(true)))

  test("Basic Select") {
    val sparkconnect = analyze(connectTestRelation.select("a"))
    val df = testRelation.select("a").queryExecution.analyzed
    comparePlans(sparkconnect, df)
  }

  private def analyze(plan: proto.Relation): LogicalPlan = {
    spark.sessionState.executePlan(transform(plan)).analyzed
  }

  protected override def comparePlans(
    plan1: LogicalPlan,
    plan2: LogicalPlan,
    checkAnalysis: Boolean = false): Unit = {
    // Analysis tests may have not been fully resolved, so skip checkAnalysis.
    super.comparePlans(plan1, plan2, checkAnalysis)
  }
}