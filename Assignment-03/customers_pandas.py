"""Load customers_raw.csv into a pandas DataFrame for analysis.

Run with: python3 Assignment-03/customers_pandas.py

The `customers` DataFrame is available here for ad-hoc queries, e.g.:
    customers.query("zone == 'North'").head()
"""

from pathlib import Path

import pandas as pd

_BASE_DIR = Path(__file__).resolve().parent
if _BASE_DIR.name == "__pycache__":  # when loaded from the .pyc file
    _BASE_DIR = _BASE_DIR.parent
CSV_PATH = _BASE_DIR / "customers_raw.csv"


def load_customers(path: Path = CSV_PATH) -> pd.DataFrame:
    """Read the raw CSV and apply basic presentation-ready cleanup."""
    df = pd.read_csv(path)

    df["customer_id"] = pd.to_numeric(df["customer_id"], errors="coerce").astype("Int64")
    df["signup_date"] = pd.to_datetime(
        df["signup_date"], format="mixed", dayfirst=False, errors="coerce"
    )
    df["phone_digits"] = df["phone"].str.replace(r"\D", "", regex=True)

    zone_aliases = {"N": "North", "Sth": "South", "E.": "East", "W": "West"}
    df["zone_clean"] = (
        df["zone"].str.strip().str.title().replace(zone_aliases)
    )

    return df


customers = load_customers()


if __name__ == "__main__":
    print(f"Loaded {len(customers):,} rows x {customers.shape[1]} columns from {CSV_PATH}")

    print("\nFirst 5 rows:")
    print(customers.head().to_string(index=False))

    print("\nColumn types:")
    print(customers.dtypes.to_string())

    print("\nMissing values per column:")
    print(customers.isna().sum().to_string())

    print("\nDuplicate customer IDs:", customers["customer_id"].duplicated().sum())

    print("\nSignup date range:")
    print(
        f"  {customers['signup_date'].min():%Y-%m-%d} to "
        f"{customers['signup_date'].max():%Y-%m-%d}"
    )

    print("\nCustomers by zone (standardized):")
    print(customers["zone_clean"].value_counts().to_string())

    print("\nCustomers by acquisition channel:")
    print(customers["acquisition_channel"].value_counts().to_string())

    print("\nSignups by month:")
    print(
        customers.groupby(customers["signup_date"].dt.to_period("M"))
        .size()
        .to_string()
    )
