from typing import List, Dict, Any, Tuple

class ValidationError(Exception):
    pass

def validate_row(row: Dict[str, Any], schema: Dict[str, Any], row_num: int) -> List[Dict[str, Any]]:
    errors = []
    fields = schema['fields']
    for field, rules in fields.items():
        value = row.get(field)
        # Required check
        if rules.get('required', False) and (value is None or value == ''):
            errors.append({
                'row': row_num,
                'column': field,
                'error': 'Missing required field'
            })
            continue
        # Type check
        if value is not None and value != '':
            expected_type = rules['type']
            if expected_type == 'number':
                try:
                    num = float(value)
                except ValueError:
                    errors.append({'row': row_num, 'column': field, 'error': 'Expected number'})
                    continue
                # Min/max
                if 'min' in rules and num < rules['min']:
                    errors.append({'row': row_num, 'column': field, 'error': f'Value below min {rules["min"]}'})
                if 'max' in rules and num > rules['max']:
                    errors.append({'row': row_num, 'column': field, 'error': f'Value above max {rules["max"]}'})
            elif expected_type == 'boolean':
                if str(value).lower() not in ('true', 'false', '1', '0'):
                    errors.append({'row': row_num, 'column': field, 'error': 'Expected boolean'})
            elif expected_type == 'string':
                if 'length' in rules and len(str(value)) != rules['length']:
                    errors.append({'row': row_num, 'column': field, 'error': f'Expected length {rules["length"]}'})
    # Unexpected columns (warning only)
    for col in row:
        if col not in fields:
            errors.append({'row': row_num, 'column': col, 'error': 'Unexpected column', 'level': 'warning'})
    return errors

def validate_csv(rows: List[Dict[str, Any]], schema: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], int]:
    all_errors = []
    for i, row in enumerate(rows, start=2):  # CSV header is row 1
        errors = validate_row(row, schema, i)
        all_errors.extend(errors)
    return all_errors, len(rows)
