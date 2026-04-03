# TROUBLESHOOT: Common Issues

## "OpenAI API key not found"
Set OPENAI_API_KEY. Use .env with python-dotenv, or export in terminal.

## "Invalid URL" or image doesn't load
DALL-E returns a URL. Gradio's Image component can load URLs. If it fails, the URL may have expired—DALL-E URLs are temporary.

## "Content policy" error
Some prompts are blocked (violence, etc.). Rephrase your prompt.

## Rate limit
OpenAI has usage limits. Wait a minute and try again. Check your API usage at platform.openai.com.
