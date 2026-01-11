# tablint

**Stop CSVs from breaking your app.**

tablint is a small, offline CLI tool that validates CSV files against a fixed schema and fails fast when something will break production.

No cloud. No AI. No surprises.

---

## Who this is for

tablint is for developers and small teams who receive CSV files from humans or partners and want validation failures to happen **before** production or CI.

If a CSV changing silently has ever broken your app, this tool is for you.

---

## Example

```bash
python -m tablint validate data.csv --schema schema.json
```

```txt
❌ Validation failed

Row 14:
- price: expected number, got "free"

Summary:
- Rows checked: 1000
- Errors found: 1
```

---

## What it does

- Deterministic CSV validation
- Simple, explicit JSON schema format
- Clear, human-readable error messages
- Optional machine-readable output (`--json`)
- Fully offline (no network calls)

---

## What it does NOT do

- No auto-fixing of data
- No schema inference
- No cloud services or APIs
- No telemetry or tracking
- No payment processing inside the tool

---

## Install

Clone the repository and run directly with Python:

```bash
git clone https://github.com/melee45/tablint.git
cd tablint
python -m tablint validate data.csv --schema schema.json
```

Python 3.9+ recommended.

---

## Usage

```bash
python -m tablint validate <csv_file> --schema <schema_file> [--json] [--quiet]
```

Options:
- `--schema` : Path to schema file (required)
- `--json`   : Output results in JSON format
- `--quiet`  : Suppress non-error output

---

## Pricing

**Free tier**
- 50 validations per month
- Fully offline
- No account required

**Pro license (one-time purchase)**
- Unlimited validations
- CI/CD usage allowed

When the free limit is reached, tablint will stop and show a clear upgrade message.

Buy Pro License: https://amimirog.gumroad.com/l/zmaku

---

## License & enforcement

tablint uses **local, offline license verification**.

- No network checks
- No telemetry
- No background services

All enforcement happens on your machine.

---

## Project status

**v1 behavior is frozen.**  
Bug fixes only. No feature creep.