# TEACH: Script for Teaching This Project

## Opening

"We're building a chatbot that reads your PDFs and answers questions from them. No more searching through documents—ask in plain English."

## Key Terms

**RAG** = Retrieval-Augmented Generation. Retrieve relevant chunks first, then generate an answer. GPT doesn't memorize your PDFs—it gets the chunks when you ask.

**Embeddings** = Turning text into numbers (vectors). Similar text = similar numbers. Lets the computer "search" by meaning.

**Vector Store** = Database of embeddings. FAISS is one. When you ask a question, we find the closest chunks.

## Demo Flow

1. Show the documents folder. "PDFs go here."
2. Run the app. "Gradio gives us a chat UI for free."
3. Ask: "What is the vacation policy?" Show how it finds and uses the PDF content.
4. Ask something not in the PDF. "It won't make things up—it only uses what it found."

## Closing

"This pattern works for any documents: manuals, policies, textbooks. Load, chunk, embed, retrieve, generate."
