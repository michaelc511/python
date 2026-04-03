# TOP 10: If You Only Remember These

1. **RAG** = Retrieve relevant chunks first, then generate. Don't send the whole document to the AI. Search, then answer.

2. **Embeddings** = Text turns into numbers. Similar text = similar numbers. Lets you search by meaning.

3. **Gradio** = One line gives you a web chat. `gr.ChatInterface(fn=your_function)` and you're done.

4. **Chunking** = Split long text into smaller pieces. GPT has limits. Chunks of 500–1000 chars work.

5. **Tools** = Functions the AI can call. The AI decides when. @tool makes a function a tool.

6. **Router** = Classify the input, then send to the right handler. One entry point, many specialized behaviors.

7. **API Key** = You need OPENAI_API_KEY for most projects. Put it in .env. Never commit it to git.

8. **Vector Store** = Holds embeddings. FAISS is one. You search for "chunks similar to my question."

9. **Agent** = LLM + tools. The AI doesn't just talk—it can do things (book, search, update) by calling tools.

10. **requirements.txt** = List of packages. `pip install -r requirements.txt` installs everything. Always include it.
