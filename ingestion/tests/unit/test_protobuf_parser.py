#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Protobuf parser tests
"""

from unittest import TestCase

from metadata.generated.schema.entity.data.table import Column
from metadata.parsers.protobuf_parser import ProtobufParser, ProtobufParserConfig


class ProtobufParserTests(TestCase):
    """
    Check methods from protobuf_parser.py
    """

    schema_name = "person_info"

    sample_protobuf_schema = """
    syntax = "proto3";
    package persons;
    enum Gender {
        M = 0; // male 
        F = 1; // female
        O = 2; // other
    }

    message Result {
        string url = 1;
        string title = 2;
        repeated string snippets = 3;
    }

    message PersonInfo {
        int32 age = 1; // age in years
        Gender gender = 2; 
        Result gender_new = 3; 
        int32 height = 4; // height in cm
        fixed32 height_new = 5; // height in cm
        bool my_bool = 6;
        repeated string repeated_string = 7;   
    }
    """

    protobuf_parser = ProtobufParser(
        config=ProtobufParserConfig(
            schema_name=schema_name, schema_text=sample_protobuf_schema
        )
    )
    parsed_schema = protobuf_parser.parse_protobuf_schema()

    def test_schema_name(self):
        self.assertEqual(self.parsed_schema[0].name.__root__, "PersonInfo")

    def test_schema_type(self):
        self.assertEqual(self.parsed_schema[0].dataType.name, "RECORD")

    def test_field_names(self):
        field_names = {
            str(field.name.__root__) for field in self.parsed_schema[0].children
        }
        self.assertEqual(
            field_names,
            {
                "height",
                "gender",
                "age",
                "gender_new",
                "height_new",
                "my_bool",
                "repeated_string",
            },
        )

    def test_field_types(self):
        field_types = {
            str(field.dataType.name) for field in self.parsed_schema[0].children
        }
        self.assertEqual(
            field_types, {"INT", "ENUM", "RECORD", "FIXED", "STRING", "BOOLEAN"}
        )

    def test_column_types(self):
        parsed_schema = self.protobuf_parser.parse_protobuf_schema(cls=Column)
        field_types = {str(field.dataType.name) for field in parsed_schema[0].children}
        self.assertEqual(field_types, {"INT", "ENUM", "RECORD", "STRING", "BOOLEAN"})
