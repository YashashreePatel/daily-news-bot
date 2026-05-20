import requests
from datetime import datetime, timedelta
from app.config import NEWS_API_KEY, SEARCH_QUERIES

def fetch_daily_news():
    if not NEWS_API_KEY:
        print("[Scraper Error]: NEWS_API_KEY is not defined inside environment keys.")
        return {}

    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    base_url = f"https://newsapi.org/v2/everything?from={yesterday}&sortBy=popularity&apiKey={NEWS_API_KEY}"
    
    categorized_news = {category: [] for category in SEARCH_QUERIES.keys()}

    for category, query in SEARCH_QUERIES.items():
        try:
            response = requests.get(f"{base_url}&q={query}&pageSize=5")
            if response.status_code == 200:
                articles = response.json().get('articles', [])
                for art in articles:
                    title = art.get('title')
                    link = art.get('url')
                    if title and link:
                        # Ensures the text string forms a tight 1-line layout
                        clean_title = title.replace("\n", " ").strip()
                        short_title = clean_title[:85] + "..." if len(clean_title) > 85 else clean_title
                        categorized_news[category].append({"summary": short_title, "link": link})
            else:
                print(f"[Scraper Warning]: Request failure for '{category}' code: {response.status_code}")
        except Exception as e:
            print(f"[Scraper Exception]: Occurred parsing '{category}': {e}")

    return categorized_news