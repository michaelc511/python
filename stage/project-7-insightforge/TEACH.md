# TEACH: Script for Teaching This Project

## Opening

"InsightForge is BI meets RAG. We have business data. Users can ask questions in plain English or get a summary. Same pattern as the HR bot, but the data is structured (CSV) instead of PDFs."

## Key Idea

"We convert rows to text: 'On Jan, Laptop sold 50 for $45k.' That text goes into RAG. So we can answer 'How did Laptop do?' with retrieval. For 'give me insights' we skip RAG and use pandas—groupby, sum, etc."

## Demo

1. Ask: "How did Laptop perform?" → RAG answer
2. Ask: "Give me insights" → Pandas summary
3. Show the CSV. "This is our source. We turn it into searchable text."

## Closing

"RAG isn't only for documents. Any data you can turn into text can be queried with natural language."
