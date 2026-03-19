# TROUBLESHOOT: Common Issues

## "OpenAI API key not found"
Set OPENAI_API_KEY in .env or environment.

## Agent doesn't use the right tool
Improve the tool's docstring. The LLM uses it to decide. Be specific: "Book a medical appointment. Requires: patient name, doctor type, date."

## create_tool_calling_agent not found
LangChain versions vary. Use: from langchain.agents import create_tool_calling_agent. If missing, try create_react_agent or check your langchain version.

## Records don't persist
We use in-memory lists/dicts. For real use, save to a database or file.
