# EXPLAIN: Nestle HR Assistant (RAG Chatbot)

## What This Does

You add HR policy PDFs to a folder. The program reads them, breaks them into chunks, and stores them in a special way (vectors). When you ask a question, it finds the most relevant chunks and sends them to GPT to write an answer. That's called **RAG** = Retrieval-Augmented Generation.

---

## Step-by-Step

### 1. Load PDFs
`PyPDFLoader` reads each PDF and turns pages into text. We put all the text into a list called `documents`.

### 2. Split into Chunks
A 50-page PDF is too big to send to GPT at once. We split it into chunks of about 1000 characters. `RecursiveCharacterTextSplitter` does this. Overlap of 200 means the last part of one chunk repeats at the start of the next—so we don't lose context at the cut.

### 3. Create Embeddings
Each chunk gets turned into a vector (a list of numbers). Similar chunks get similar vectors. We use `OpenAIEmbeddings()` to do this. You need an OpenAI API key.

### 4. Store in FAISS
FAISS is a library that stores vectors and lets you search for "which chunks are most similar to my question?" Fast search.

### 5. Retrieval QA Chain
When you ask "What is the vacation policy?":
1. Your question gets embedded
2. FAISS finds the 3 most similar chunks
3. Those chunks + your question go to GPT
4. GPT writes an answer using only that context

### 6. Gradio
Gradio gives you a web chat interface. No need to build a website—one line `gr.ChatInterface()` does it.

---

## Setup Required

1. Create folder `documents/` and add your Nestle HR PDFs
2. Set `OPENAI_API_KEY` in environment or `.env` file
3. Run `pip install -r requirements.txt`
4. Run `python hr_assistant.py`
