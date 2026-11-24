"""Import the customers_raw.csv file from the Assignment-03 folder."""

import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent / "customers_raw.csv"


def load_customers(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


if __name__ == "__main__":
    customers = load_customers(CSV_PATH)

    print(f"Imported {len(customers)} rows from {CSV_PATH}")
    print(f"Columns: {', '.join(customers[0].keys()) if customers else 'none'}")
    print("\nFirst 5 rows:")
    for row in customers[:5]:
        print(row)
