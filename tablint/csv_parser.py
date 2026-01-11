import csv
from typing import List, Dict, Any

def parse_csv(file_path: str) -> List[Dict[str, Any]]:
    """Parse a CSV file and return a list of rows as dictionaries."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
