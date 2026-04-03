"""
NewsGenie – An AI-Powered Information and News Assistant
Combines general chatbot with real-time news for technology, finance, and sports.
"""

import os
import requests
from openai import OpenAI
import gradio as gr

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# News API - get free key at newsapi.org
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "your-news-api-key")
NEWS_URL = "https://newsapi.org/v2/top-headlines"


def get_news(category):
    """Fetch real-time news for a category (technology, business, sports)."""
    params = {
        "apiKey": NEWS_API_KEY,
        "category": category,
        "pageSize": 5,
        "country": "us",
    }
    try:
        response = requests.get(NEWS_URL, params=params)
        data = response.json()
        if data.get("status") == "ok" and data.get("articles"):
            articles = data["articles"]
            text = f"\n\n--- {category.upper()} NEWS ---\n\n"
            for i, art in enumerate(articles[:5], 1):
                title = art.get("title", "No title")
                desc = art.get("description", "") or ""
                text += f"{i}. {title}\n   {desc[:100]}...\n\n"
            return text
    except Exception as e:
        return f"Could not fetch news: {e}"
    return "No news available for this category."


def is_news_query(message):
    """Simple check: does the user want news?"""
    message_lower = message.lower()
    news_words = ["news", "headlines", "technology", "finance", "sports", "latest", "today"]
    return any(word in message_lower for word in news_words)


def get_category_from_message(message):
    """Guess which news category from the message."""
    message_lower = message.lower()
    if "tech" in message_lower or "technology" in message_lower:
        return "technology"
    if "finance" in message_lower or "business" in message_lower or "money" in message_lower:
        return "business"
    if "sport" in message_lower or "sports" in message_lower:
        return "sports"
    return "technology"  # default


def chat_response(message, history):
    """Handle user message: news or general chat."""
    if is_news_query(message):
        category = get_category_from_message(message)
        news_text = get_news(category)
        return news_text
    else:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content


demo = gr.ChatInterface(
    fn=chat_response,
    title="NewsGenie",
    description="Ask for news (technology, finance, sports) or ask general questions.",
)

if __name__ == "__main__":
    demo.launch()
