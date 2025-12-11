# Property Insight Summarizer

The Property Insight Summarizer is a lightweight data-processing pipeline that turns raw real estate listings into structured, investor-friendly insights using OpenAI GPT-5.
It ingests property data (CSV), normalizes key attributes, and enriches each listing with AI-generated summaries, investment scoring, risks, and recommended actions.

# Project Structure
│ └─ sample_listing_pages/ # optional local HTMLs if you prefer
├─ src/
│ ├─ ingest.py
│ ├─ scrape_listings.py
│ ├─ normalize.py
│ ├─ extract_llm.py
│ └─ main.py
└─ outputs/
├─ enriched_listings.json
└─ enriched_listings.csv

## Quick start

1. Create & activate a virtual environment:

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
# venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Set your OpenAI API key and model:

```bash
export OPENAI_API_KEY=sk-...
OPENAI_MODEL=your_openai_model
# Or create a .env file with OPENAI_API_KEY=...

```

4. Put you data in `sample_listings.csv` in `sample_data/`.


5. Run the pipeline:

```bash
python src/main.py
```

6. Find outputs in `outputs/enriched_listings.json` and `outputs/enriched_listings.csv`.

