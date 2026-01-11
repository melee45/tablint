import json
from typing import Dict, Any

class SchemaError(Exception):
    pass

def parse_schema(file_path: str) -> Dict[str, Any]:
    """Parse a schema file (JSON) and return the schema as a dictionary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        # Basic validation of schema structure
        if not isinstance(schema, dict) or 'fields' not in schema:
            raise SchemaError('Schema must be a JSON object with a "fields" key.')
        for field, rules in schema['fields'].items():
            if 'type' not in rules or rules['type'] not in ('string', 'number', 'boolean'):
                raise SchemaError(f'Field {field} must specify a valid type.')
        return schema
    except Exception as e:
        raise SchemaError(f'Invalid schema: {e}')
