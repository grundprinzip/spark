#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DataType(google.protobuf.message.Message):
    """This message describes the logical [[DataType]] of something. It does not carry the value
    itself but only describes it.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Boolean(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class I8(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class I16(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class I32(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class I64(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class FP32(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class FP64(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class String(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Binary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Timestamp(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Date(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Time(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class TimestampTZ(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class IntervalYear(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class IntervalDay(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class UUID(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class FixedChar(google.protobuf.message.Message):
        """Start compound types."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        length: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            length: builtins.int = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "length", b"length", "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class VarChar(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        length: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            length: builtins.int = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "length", b"length", "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class FixedBinary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LENGTH_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        length: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            length: builtins.int = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "length", b"length", "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class Decimal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SCALE_FIELD_NUMBER: builtins.int
        PRECISION_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        scale: builtins.int
        precision: builtins.int
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            scale: builtins.int = ...,
            precision: builtins.int = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "precision",
                b"precision",
                "scale",
                b"scale",
                "type_variation_reference",
                b"type_variation_reference",
            ],
        ) -> None: ...

    class StructField(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class MetadataEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            value: builtins.str
            def __init__(
                self,
                *,
                key: builtins.str = ...,
                value: builtins.str = ...,
            ) -> None: ...
            def ClearField(
                self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
            ) -> None: ...

        TYPE_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        NULLABLE_FIELD_NUMBER: builtins.int
        METADATA_FIELD_NUMBER: builtins.int
        @property
        def type(self) -> global___DataType: ...
        name: builtins.str
        nullable: builtins.bool
        @property
        def metadata(
            self,
        ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
        def __init__(
            self,
            *,
            type: global___DataType | None = ...,
            name: builtins.str = ...,
            nullable: builtins.bool = ...,
            metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["type", b"type"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "metadata", b"metadata", "name", b"name", "nullable", b"nullable", "type", b"type"
            ],
        ) -> None: ...

    class Struct(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FIELDS_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        @property
        def fields(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
            global___DataType.StructField
        ]: ...
        type_variation_reference: builtins.int
        def __init__(
            self,
            *,
            fields: collections.abc.Iterable[global___DataType.StructField] | None = ...,
            type_variation_reference: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "fields", b"fields", "type_variation_reference", b"type_variation_reference"
            ],
        ) -> None: ...

    class List(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        DATATYPE_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        ELEMENT_NULLABLE_FIELD_NUMBER: builtins.int
        @property
        def DataType(self) -> global___DataType: ...
        type_variation_reference: builtins.int
        element_nullable: builtins.bool
        def __init__(
            self,
            *,
            DataType: global___DataType | None = ...,
            type_variation_reference: builtins.int = ...,
            element_nullable: builtins.bool = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["DataType", b"DataType"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "DataType",
                b"DataType",
                "element_nullable",
                b"element_nullable",
                "type_variation_reference",
                b"type_variation_reference",
            ],
        ) -> None: ...

    class Map(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        TYPE_VARIATION_REFERENCE_FIELD_NUMBER: builtins.int
        VALUE_NULLABLE_FIELD_NUMBER: builtins.int
        @property
        def key(self) -> global___DataType: ...
        @property
        def value(self) -> global___DataType: ...
        type_variation_reference: builtins.int
        value_nullable: builtins.bool
        def __init__(
            self,
            *,
            key: global___DataType | None = ...,
            value: global___DataType | None = ...,
            type_variation_reference: builtins.int = ...,
            value_nullable: builtins.bool = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "key",
                b"key",
                "type_variation_reference",
                b"type_variation_reference",
                "value",
                b"value",
                "value_nullable",
                b"value_nullable",
            ],
        ) -> None: ...

    BOOL_FIELD_NUMBER: builtins.int
    I8_FIELD_NUMBER: builtins.int
    I16_FIELD_NUMBER: builtins.int
    I32_FIELD_NUMBER: builtins.int
    I64_FIELD_NUMBER: builtins.int
    FP32_FIELD_NUMBER: builtins.int
    FP64_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    BINARY_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    DATE_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    INTERVAL_YEAR_FIELD_NUMBER: builtins.int
    INTERVAL_DAY_FIELD_NUMBER: builtins.int
    TIMESTAMP_TZ_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    FIXED_CHAR_FIELD_NUMBER: builtins.int
    VARCHAR_FIELD_NUMBER: builtins.int
    FIXED_BINARY_FIELD_NUMBER: builtins.int
    DECIMAL_FIELD_NUMBER: builtins.int
    STRUCT_FIELD_NUMBER: builtins.int
    LIST_FIELD_NUMBER: builtins.int
    MAP_FIELD_NUMBER: builtins.int
    USER_DEFINED_TYPE_REFERENCE_FIELD_NUMBER: builtins.int
    @property
    def bool(self) -> global___DataType.Boolean: ...
    @property
    def i8(self) -> global___DataType.I8: ...
    @property
    def i16(self) -> global___DataType.I16: ...
    @property
    def i32(self) -> global___DataType.I32: ...
    @property
    def i64(self) -> global___DataType.I64: ...
    @property
    def fp32(self) -> global___DataType.FP32: ...
    @property
    def fp64(self) -> global___DataType.FP64: ...
    @property
    def string(self) -> global___DataType.String: ...
    @property
    def binary(self) -> global___DataType.Binary: ...
    @property
    def timestamp(self) -> global___DataType.Timestamp: ...
    @property
    def date(self) -> global___DataType.Date: ...
    @property
    def time(self) -> global___DataType.Time: ...
    @property
    def interval_year(self) -> global___DataType.IntervalYear: ...
    @property
    def interval_day(self) -> global___DataType.IntervalDay: ...
    @property
    def timestamp_tz(self) -> global___DataType.TimestampTZ: ...
    @property
    def uuid(self) -> global___DataType.UUID: ...
    @property
    def fixed_char(self) -> global___DataType.FixedChar: ...
    @property
    def varchar(self) -> global___DataType.VarChar: ...
    @property
    def fixed_binary(self) -> global___DataType.FixedBinary: ...
    @property
    def decimal(self) -> global___DataType.Decimal: ...
    @property
    def struct(self) -> global___DataType.Struct: ...
    @property
    def list(self) -> global___DataType.List: ...
    @property
    def map(self) -> global___DataType.Map: ...
    user_defined_type_reference: builtins.int
    def __init__(
        self,
        *,
        bool: global___DataType.Boolean | None = ...,
        i8: global___DataType.I8 | None = ...,
        i16: global___DataType.I16 | None = ...,
        i32: global___DataType.I32 | None = ...,
        i64: global___DataType.I64 | None = ...,
        fp32: global___DataType.FP32 | None = ...,
        fp64: global___DataType.FP64 | None = ...,
        string: global___DataType.String | None = ...,
        binary: global___DataType.Binary | None = ...,
        timestamp: global___DataType.Timestamp | None = ...,
        date: global___DataType.Date | None = ...,
        time: global___DataType.Time | None = ...,
        interval_year: global___DataType.IntervalYear | None = ...,
        interval_day: global___DataType.IntervalDay | None = ...,
        timestamp_tz: global___DataType.TimestampTZ | None = ...,
        uuid: global___DataType.UUID | None = ...,
        fixed_char: global___DataType.FixedChar | None = ...,
        varchar: global___DataType.VarChar | None = ...,
        fixed_binary: global___DataType.FixedBinary | None = ...,
        decimal: global___DataType.Decimal | None = ...,
        struct: global___DataType.Struct | None = ...,
        list: global___DataType.List | None = ...,
        map: global___DataType.Map | None = ...,
        user_defined_type_reference: builtins.int = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "binary",
            b"binary",
            "bool",
            b"bool",
            "date",
            b"date",
            "decimal",
            b"decimal",
            "fixed_binary",
            b"fixed_binary",
            "fixed_char",
            b"fixed_char",
            "fp32",
            b"fp32",
            "fp64",
            b"fp64",
            "i16",
            b"i16",
            "i32",
            b"i32",
            "i64",
            b"i64",
            "i8",
            b"i8",
            "interval_day",
            b"interval_day",
            "interval_year",
            b"interval_year",
            "kind",
            b"kind",
            "list",
            b"list",
            "map",
            b"map",
            "string",
            b"string",
            "struct",
            b"struct",
            "time",
            b"time",
            "timestamp",
            b"timestamp",
            "timestamp_tz",
            b"timestamp_tz",
            "user_defined_type_reference",
            b"user_defined_type_reference",
            "uuid",
            b"uuid",
            "varchar",
            b"varchar",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "binary",
            b"binary",
            "bool",
            b"bool",
            "date",
            b"date",
            "decimal",
            b"decimal",
            "fixed_binary",
            b"fixed_binary",
            "fixed_char",
            b"fixed_char",
            "fp32",
            b"fp32",
            "fp64",
            b"fp64",
            "i16",
            b"i16",
            "i32",
            b"i32",
            "i64",
            b"i64",
            "i8",
            b"i8",
            "interval_day",
            b"interval_day",
            "interval_year",
            b"interval_year",
            "kind",
            b"kind",
            "list",
            b"list",
            "map",
            b"map",
            "string",
            b"string",
            "struct",
            b"struct",
            "time",
            b"time",
            "timestamp",
            b"timestamp",
            "timestamp_tz",
            b"timestamp_tz",
            "user_defined_type_reference",
            b"user_defined_type_reference",
            "uuid",
            b"uuid",
            "varchar",
            b"varchar",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["kind", b"kind"]
    ) -> typing_extensions.Literal[
        "bool",
        "i8",
        "i16",
        "i32",
        "i64",
        "fp32",
        "fp64",
        "string",
        "binary",
        "timestamp",
        "date",
        "time",
        "interval_year",
        "interval_day",
        "timestamp_tz",
        "uuid",
        "fixed_char",
        "varchar",
        "fixed_binary",
        "decimal",
        "struct",
        "list",
        "map",
        "user_defined_type_reference",
    ] | None: ...

global___DataType = DataType
