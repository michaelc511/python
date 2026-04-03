# TROUBLESHOOT: Common Issues

## "Could not fetch news"
Check NEWS_API_KEY. Get a free key at newsapi.org. Set it in .env or environment.

## Always gets GPT instead of news
Your message might not have news keywords. Try "Give me technology news" or "Latest headlines". Check is_news_query() logic.

## News API rate limit
Free tier has limits. If you hit it, wait or upgrade.

## Wrong category
get_category_from_message is simple keyword match. Add more words if needed.
