# EXPLAIN: NewsGenie

## What This Does

One app, two modes:
1. **News mode** – User asks for news (tech, finance, sports). We call NewsAPI, get headlines, show them.
2. **Chat mode** – User asks a general question. We send it to GPT, get an answer.

We decide which mode by checking the message. If it has words like "news", "headlines", "technology", we fetch news. Otherwise we use GPT.

---

## Key Parts

### is_news_query()
Checks if the message contains news-related words. Simple but works for most cases.

### get_category_from_message()
Looks at the message and picks technology, business, or sports. Defaults to technology.

### get_news()
Calls newsapi.org with the category. Returns formatted headlines. Needs NEWS_API_KEY (free at newsapi.org).

### chat_response()
The main function. If news query → get_news(). Else → call GPT. Returns the result to Gradio.

---

## Error Handling

If NewsAPI fails (bad key, network issue), we return a message. The app doesn't crash. For production you'd add a fallback (e.g., show cached news or a friendly error).
