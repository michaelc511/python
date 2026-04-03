# EXPLAIN: InsightForge (BI + RAG)

## What This Does

Combines:
1. **RAG on business data** – Sales data (CSV) turned into text chunks, embedded, stored. You ask "How did Laptop perform?" and it finds the right chunks.
2. **Simple insights** – If you ask for "insights" or "summary", we compute totals, best product, trend from the dataframe.
3. **Gradio chat** – One interface for both.

---

## Data Flow

1. Load CSV (or use sample data)
2. Turn each row into a sentence: "On 2024-01, Laptop sold 50 units for $45000."
3. Chunk, embed, store in FAISS
4. User asks question → RAG finds chunks → GPT answers
5. Or user asks "insights" → we run pandas groupby/sum → return summary

---

## Why Both RAG and Direct Calc?

RAG is good for "What happened with X?" — natural language. Direct calc is good for "Give me the summary" — we control the metrics. Together they cover both.
