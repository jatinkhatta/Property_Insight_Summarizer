import os
import time
import json
from typing import Dict, Any
from openai import OpenAI

def client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = """
You are a real estate investment assistant. Given this property JSON, output ONLY valid JSON with:
- summary (2-3 sentences)
- investment_score (0-100)
- score_breakdown {location, condition, cashflow, appreciation_potential}
- pitch (1-2 sentences)
- top_risks (2-4 items)
- suggested_actions (2-4 items)

Input:
{listing}

Output JSON only.
"""

def build_messages(listing):
    return [
        {"role": "system", "content": "Return only JSON."},
        {"role": "user", "content": PROMPT.format(listing=json.dumps(listing))}
    ]

def enrich_listing(listing: Dict[str, Any], model=None):
    cli = client()
    model = model or os.getenv("OPENAI_MODEL") or "gpt-5"

    messages = build_messages(listing)

    resp = cli.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=350,
        temperature=0.2
    )

    text = resp.choices[0].message.content.strip()
    enriched = json.loads(text)
    enriched["_source_id"] = listing.get("id")
    return enriched

if __name__ == "__main__":
    print(enrich_listing({"id": "1", "title": "House"}))
