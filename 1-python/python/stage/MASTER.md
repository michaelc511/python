# MASTER: How All 9 Projects Connect

## The Big Picture

These 9 projects build from basic Python to AI applications. Each one adds a new layer.

---

## The Arc

| # | Project | What You Learn | Builds On |
|---|---------|----------------|----------|
| 1 | Adventure Game | Variables, lists, dicts, loops, functions | Pure Python basics |
| 2 | Customer Orders | Data structures for analysis | Same basics, now with real data |
| 3 | ChatGPT Storytelling | Prompting, no code | Understanding AI as a tool |
| 4 | Nestle HR Assistant | RAG, PDFs → chatbot | First real AI app: load docs, embed, retrieve, generate |
| 5 | OpenAI + Gradio | API calls, image generation | Same pattern: API + Gradio UI |
| 6 | NewsGenie | Query routing, multiple services | Combine GPT + external API (news) |
| 7 | InsightForge | RAG on structured data, BI | RAG + pandas, data as text |
| 8 | Agentic Healthcare | Tools, agent picks what to do | LLM + tools = agent |
| 9 | Banking Multi-Agent | Router, multiple handlers | Classify → route → specialized response |

---

## Core Patterns That Repeat

1. **Input → Process → Output** – Every project. User gives input, we process, we return output.
2. **Gradio** – Projects 4, 5, 6, 7, 8, 9. One library for chat/UI. Same pattern.
3. **RAG** – Projects 4 and 7. Load, chunk, embed, retrieve, generate. Same pipeline.
4. **Routing** – Projects 6 and 9. Decide where the request goes based on content.
5. **Tools/Agents** – Projects 8 and 9. Give the AI things it can do. It picks when to use them.

---

## Dependencies You'll Need

- **Projects 1–3**: None (or just Python)
- **Projects 4–9**: OpenAI API key
- **Project 4**: PDFs in documents/
- **Project 6**: News API key
- **Projects 4, 7, 8**: LangChain, FAISS (for 4, 7)

---

## Study Order

Do 1 → 2 → 3 first. Basics and prompting.  
Then 4 → 5 → 6. APIs and RAG.  
Then 7 → 8 → 9. BI, agents, multi-agent.
