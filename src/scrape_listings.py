import requests
from bs4 import BeautifulSoup
from typing import Dict

def scrape_url(url: str) -> Dict:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    title = soup.title.string.strip() if soup.title else ""
    meta = soup.find("meta", {"name": "description"})
    description = meta["content"].strip() if meta and "content" in meta.attrs else ""

    if not description:
        paragraphs = "\n".join(p.get_text(strip=True) for p in soup.find_all("p")[:5])
        description = paragraphs

    return {"url": url, "title": title, "description": description}

if __name__ == "__main__":
    print(scrape_url("https://example.com"))
