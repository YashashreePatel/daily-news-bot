from app.scraper import fetch_daily_news
from app.notifier import send_telegram_notifications
from app.database import has_been_sent, mark_as_sent

def main():
    print("Initiating daily categorized news sequence...")
    all_news = fetch_daily_news()
    filtered_news = {}

    for category, articles in all_news.items():
        filtered_news[category] = []
        for item in articles:
            # Dedup checks prior to building individual messages
            if not has_been_sent(item['link']):
                filtered_news[category].append(item)
                mark_as_sent(item['link'])

    # Execute isolated notifications back-to-back
    send_telegram_notifications(filtered_news)
    print("Daily pipeline execution finalized.")

if __name__ == "__main__":
    main()