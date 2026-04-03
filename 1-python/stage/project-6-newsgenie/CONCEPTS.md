# CONCEPTS: What You Need to Know

## Query Routing
Deciding which service to use based on what the user asked. News → News API. General question → GPT.

## REST API
Web service you call with HTTP. newsapi.org is one. You send a URL with parameters, get JSON back.

## Fallback
When one service fails, have a backup. Here we return an error message. Better: show cached news or "Try again later."
