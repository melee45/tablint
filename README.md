# tablint

**Stop CSVs from breaking your app.**

tablint is a small, offline CLI tool that validates CSV files against a fixed schema and fails fast when something will break production.

No cloud. No AI. No surprises.

👉 Product overview, pricing, and commercial license:
**https://melee45.github.io/tablint/**
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
- Explicit, fixed JSON schema
- Clear, human-readable error messages
- Optional machine-readable output (`--json`)
- Fully offline (no network calls)

---

## What it does NOT do

- No auto-fixing of data
- No schema inference
- No AI or heuristics
- No cloud services or APIs
- No telemetry or tracking

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

## Licensing

tablint includes a free evaluation mode with limited validations.

For production use and CI/CD pipelines, a Pro license is required.

- One-time purchase
- Unlimited validations
- CI/CD usage allowed
- Fully offline

👉 Details and purchase:

**https://melee45.github.io/tablint/**

---

## License enforcement

All license enforcement is local and offline.

- No network checks
- No telemetry
- No background services

The tool never phones home.

---

## Project status

**v1 behavior is frozen.**  
Bug fixes only. No feature creep.

**https://github.com/melee45/tablint**