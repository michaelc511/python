# CONCEPTS: What You Need to Know

## RAG (Retrieval-Augmented Generation)
Instead of sending all your documents to the AI, you: (1) search for the most relevant parts, (2) send only those to the AI. Saves tokens and gives accurate answers from your data.

## Embeddings
Text → list of numbers. "Vacation policy" and "leave policy" get similar numbers. The AI uses this to find related text.

## Chunking
Splitting long documents into smaller pieces. GPT has a limit. Chunks of ~1000 characters work well.

## Vector Store
A database that holds embeddings. You search by "which chunks are closest to my question's embedding?" FAISS is fast and runs on your machine.

## Gradio
Library that creates a web UI from a Python function. One decorator or interface call = chat box, no HTML/JS needed.
