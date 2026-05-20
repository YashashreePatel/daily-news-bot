import json
import os

DB_FILE = "sent_links.json"

def _load_db():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def has_been_sent(url):
    sent_urls = _load_db()
    return url in sent_urls

def mark_as_sent(url):
    sent_urls = _load_db()
    if url not in sent_urls:
        sent_urls.append(url)
        # Keep DB size light (retain last 500 records)
        if len(sent_urls) > 500:
            sent_urls = sent_urls[-500:]
        with open(DB_FILE, "w") as f:
            json.dump(sent_urls, f, indent=4)