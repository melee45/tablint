import unittest
from tablint.validator import validate_row

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.schema = {
            "fields": {
                "name": {"type": "string", "required": True, "length": 4},
                "age": {"type": "number", "min": 0, "max": 120},
                "active": {"type": "boolean"}
            }
        }

    def test_valid_row(self):
        row = {"name": "John", "age": "30", "active": "true"}
        errors = validate_row(row, self.schema, 2)
        self.assertEqual(len([e for e in errors if e.get('level', 'error') != 'warning']), 0)

    def test_missing_required(self):
        row = {"age": "30", "active": "true"}
        errors = validate_row(row, self.schema, 2)
        self.assertTrue(any(e['error'] == 'Missing required field' for e in errors))

    def test_type_and_range(self):
        row = {"name": "Jane", "age": "200", "active": "yes"}
        errors = validate_row(row, self.schema, 2)
        self.assertTrue(any('above max' in e['error'] for e in errors))
        self.assertTrue(any('Expected boolean' in e['error'] for e in errors))

    def test_length(self):
        row = {"name": "Jo", "age": "20", "active": "false"}
        errors = validate_row(row, self.schema, 2)
        self.assertTrue(any('Expected length' in e['error'] for e in errors))

    def test_unexpected_column(self):
        row = {"name": "John", "age": "30", "active": "true", "extra": "foo"}
        errors = validate_row(row, self.schema, 2)
        self.assertTrue(any(e.get('level') == 'warning' for e in errors))

if __name__ == "__main__":
    unittest.main()
