"""Validate the released CSV files."""
import hashlib
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ROWS = 1000


def check(path: Path) -> None:
    df = pd.read_csv(path)
    assert len(df) == EXPECTED_ROWS, f"{path.name}: expected {EXPECTED_ROWS} rows, got {len(df)}"
    assert df["_primaryKey"].is_unique, f"{path.name}: duplicate _primaryKey values"
    print(f"OK  {path.name}: {df.shape[0]} rows x {df.shape[1]} columns  "
          f"md5={hashlib.md5(path.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    for name in ("car_listings_clean_1000.csv", "car_listings_clean_1000_classified.csv"):
        check(ROOT / "data" / name)
    sys.exit(0)
