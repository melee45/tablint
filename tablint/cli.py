from .csv_parser import parse_csv
from .schema_parser import parse_schema, SchemaError
from .validator import validate_csv
from .license import check_license, LicenseError
from .usage_counter import check_and_increment
import argparse
import sys
import json as _json

def main():
	parser = argparse.ArgumentParser(
		description="csv-guard: Validate CSV files against a schema."
	)
	parser.add_argument(
		"validate",
		help="Validate a CSV file against a schema.",
		nargs='?'
	)
	parser.add_argument(
		"csv_file",
		help="Path to the CSV file to validate.",
		nargs='?'
	)
	parser.add_argument(
		"--schema",
		help="Path to the schema file.",
		required=False
	)
	parser.add_argument(
		"--json",
		help="Output results in JSON format.",
		action="store_true"
	)
	parser.add_argument(
		"--quiet",
		help="Suppress non-error output.",
		action="store_true"
	)
	args = parser.parse_args()

	if args.validate:
		if not args.csv_file or not args.schema:
			print("Error: csv_file and --schema are required.", file=sys.stderr)
			sys.exit(1)
		try:

			from .license import get_license_tier, LicenseError
			try:
				tier = get_license_tier()
			except LicenseError as e:
				print(f"License error: {e}", file=sys.stderr)
				sys.exit(1)

			# Usage counter enforcement (only for free tier)
			if tier == 'free':
				try:
					check_and_increment('free')
				except Exception as e:
					print(f"Usage error: {e}", file=sys.stderr)
					sys.exit(1)

			rows = parse_csv(args.csv_file)
			schema = parse_schema(args.schema)
			errors, total = validate_csv(rows, schema)

			if args.json:
				output = {
					'errors': errors,
					'total_rows': total,
					'error_count': len([e for e in errors if e.get('level') != 'warning']),
					'warning_count': len([e for e in errors if e.get('level') == 'warning'])
				}
				print(_json.dumps(output, indent=2))
			else:
				if not args.quiet:
					print(f"Validated {total} rows.")
				for err in errors:
					level = err.get('level', 'error').upper()
					print(f"{level}: Row {err['row']} Col '{err['column']}': {err['error']}")
				if not args.quiet:
					print(f"{len([e for e in errors if e.get('level') != 'warning'])} errors, {len([e for e in errors if e.get('level') == 'warning'])} warnings.")
			sys.exit(1 if any(e for e in errors if e.get('level') != 'warning') else 0)
		except FileNotFoundError as e:
			print(f"File not found: {e}", file=sys.stderr)
			sys.exit(1)
		except SchemaError as e:
			print(f"Schema error: {e}", file=sys.stderr)
			sys.exit(1)
		except Exception as e:
			print(f"Validation failed: {e}", file=sys.stderr)
			sys.exit(1)
	else:
		parser.print_help()
