import requests
from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_notifications(categorized_news):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[Notifier Error]: Missing primary Telegram target parameters.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    for category, articles in categorized_news.items():
        if not articles:
            continue
        
        # Build out an independent single text message layout per block
        message_lines = [f"🌐 *{category.upper()}* 🌐\n"]
        
        for idx, item in enumerate(articles, start=1):
            line = f"{idx}. [{item['summary']}]({item['link']})"
            message_lines.append(line)
        
        full_message = "\n".join(message_lines)
        
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": full_message,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True
        }
        
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"[Telegram Failure]: Segment '{category}' message did not submit: {response.text}")