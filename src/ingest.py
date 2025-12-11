import os
import pandas as pd
from typing import List, Dict

SAMPLE_CSV = os.path.join(os.path.dirname(__file__), "..", "sample_data", "sample_listings.csv")

def read_csv(path: str = None) -> List[Dict]:
    path = path or os.getenv("LISTINGS_CSV") or SAMPLE_CSV
    df = pd.read_csv(path, dtype=str).fillna("")
    return df.to_dict(orient="records")

if __name__ == "__main__":
    recs = read_csv()
    print(f"Loaded {len(recs)} records")
