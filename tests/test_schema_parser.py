import unittest
from tablint.schema_parser import parse_schema, SchemaError
import os
import json

class TestSchemaParser(unittest.TestCase):
    def setUp(self):
        self.valid_schema = {
            "fields": {
                "name": {"type": "string", "required": True},
                "age": {"type": "number", "min": 0, "max": 120},
                "active": {"type": "boolean"}
            }
        }
        self.invalid_schema = {"foo": "bar"}
        self.schema_path = "test_schema.json"
        with open(self.schema_path, 'w', encoding='utf-8') as f:
            json.dump(self.valid_schema, f)

    def tearDown(self):
        if os.path.exists(self.schema_path):
            os.remove(self.schema_path)

    def test_valid_schema(self):
        schema = parse_schema(self.schema_path)
        self.assertIn("fields", schema)
        self.assertIn("name", schema["fields"])

    def test_invalid_schema(self):
        with open(self.schema_path, 'w', encoding='utf-8') as f:
            json.dump(self.invalid_schema, f)
        with self.assertRaises(SchemaError):
            parse_schema(self.schema_path)

if __name__ == "__main__":
    unittest.main()
