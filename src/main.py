import json
import argparse
from pathlib import Path
import pandas as pd
from tqdm import tqdm

from ingest import read_csv
from normalize import normalize_listing
from extract_llm import enrich_listing

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def pipeline(csv_path=None, max_items=None, model=None):
    records = read_csv(csv_path)
    if max_items:
        records = records[:max_items]

    normalized = [normalize_listing(r) for r in records]
    enriched = []

    for rec in tqdm(normalized, desc="Enriching"):
        try:
            enriched_rec = enrich_listing(rec, model=model)
        except Exception as e:
            enriched_rec = {"_source_id": rec.get("id"), "error": str(e)}
        enriched.append({**rec, **enriched_rec})

    # JSON
    json_path = OUTPUT_DIR / "enriched_listings.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2)

    # CSV
    rows = []
    for it in enriched:
        rows.append({
            "id": it.get("id") or it.get("_source_id"),
            "title": it.get("title"),
            "price": it.get("price"),
            "beds": it.get("beds"),
            "baths": it.get("baths"),
            "sqft": it.get("sqft"),
            "summary": it.get("summary", ""),
            "investment_score": it.get("investment_score", ""),
            "llm_json": json.dumps(it, ensure_ascii=False)
        })

    pd.DataFrame(rows).to_csv(OUTPUT_DIR / "enriched_listings.csv", index=False)
    print("Wrote outputs.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv")
    parser.add_argument("--max", type=int)
    parser.add_argument("--model")
    args = parser.parse_args()

    pipeline(args.csv, args.max, args.model)
        