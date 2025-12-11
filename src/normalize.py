import re
from typing import Dict, Any

def parse_price(v):
    if not v: return None
    s = re.sub(r"[^0-9]", "", str(v))
    return int(s) if s else None

def parse_int(v):
    if not v: return None
    s = re.sub(r"[^0-9]", "", str(v))
    return int(s) if s else None

def normalize_listing(raw: Dict[str, Any]) -> Dict[str, Any]:
    out = raw.copy()
    out["price"] = parse_price(raw.get("price"))
    out["beds"] = parse_int(raw.get("beds"))
    out["baths"] = parse_int(raw.get("baths"))
    out["sqft"] = parse_int(raw.get("sqft"))
    return out

if __name__ == "__main__":
    print(normalize_listing({"price": "$450,000", "beds": "3"}))
