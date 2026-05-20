# Daily News Dispatcher

An automated Python bot that fetches top daily headlines via NewsAPI, categorizes them into 5 distinct topics, tracks sent links via JSON to avoid duplicates, and sends them as separate messages to Telegram using GitHub Actions.

## Project Structure
```text
news-telegram-bot/
├── .github/workflows/daily.yml
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── daily.py
│   ├── database.py
│   ├── notifier.py
│   └── scraper.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Features & Categories
- **Targeted Feeds**: Delivers 5 isolated daily Telegram messages for:
  - Tech News
  - Trading News
  - Geopolitics News
  - Where World is Today
  - All India News
- **Clean Layout**: Formats headlines into a strict 1-line summary embedded with direct source hyperlinks.
- **Smart Deduplication**: Employs a local JSON tracker (`sent_links.json`) to guarantee zero duplicate alerts.
- **Zero-Maintenance Hosting**: Automates daily dispatches completely via GitHub Actions cron scheduling.


## Quick Start (Local Setup)
### 1. Environment Setup
Clone the repo, set up your virtual environment, and install requirements:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### 2. Configure your variables inside `.env`:
```bash
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
NEWS_API_KEY=your_newsapi_org_key
```

### 2. Run the Pipeline
```python
app/daily.py
```

## GitHub Actions Deployment
The system is configured to run entirely for free via GitHub Actions (`.github/workflows/daily.yml`) every morning at 4:00 AM UTC.

### Activation Steps:
- Go to your GitHub Repository **Settings*** $\rightarrow$ **Secrets and variables** $\rightarrow$ **Actions**.
- Add the following repository secrets:
  - `TELEGRAM_BOT_TOKEN`
  - `TELEGRAM_CHAT_ID`
  - `NEWS_API_KEY`
- Head over to the **Actions** tab to manually trigger a workflow test.