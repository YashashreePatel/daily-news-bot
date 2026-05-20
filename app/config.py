import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Configuration Targets
CATEGORIES = [
    "Tech News", 
    "Trading News", 
    "Geopolitics News", 
    "Where World is Today", 
    "All India News"
]

# Queries designed specifically for NewsAPI
SEARCH_QUERIES = {
    "Tech News": "technology OR tech",
    "Trading News": "trading OR stocks OR crypto OR market",
    "Geopolitics News": "geopolitics OR international relations OR foreign policy",
    "Where World is Today": "world news OR global crisis OR international events",
    "All India News": "India OR New Delhi OR Mumbai"
}