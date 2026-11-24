"""Load the customers DataFrame from customers_pandas.cpython-313.pyc.

Open this file in Visual Studio Code and run it to get the `customers`
DataFrame without executing the .py source file directly.
"""

from importlib.machinery import SourcelessFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PYC_PATH = BASE_DIR / "__pycache__" / "customers_pandas.cpython-313.pyc"


def load_from_pyc():
    """Execute the compiled module and return its customers DataFrame."""
    loader = SourcelessFileLoader("customers_pandas", str(PYC_PATH))
    spec = spec_from_loader(loader.name, loader)
    module = module_from_spec(spec)
    loader.exec_module(module)
    return module.customers


customers = load_from_pyc()


if __name__ == "__main__":
    print(f"Loaded {len(customers):,} rows x {customers.shape[1]} columns from {PYC_PATH}")
    print("\nFirst 5 rows:")
    print(customers.head().to_string(index=False))

    print("\nCustomers by zone (standardized):")
    print(customers["zone_clean"].value_counts().to_string())

    print("\nCustomers by acquisition channel:")
    print(customers["acquisition_channel"].value_counts().to_string())
