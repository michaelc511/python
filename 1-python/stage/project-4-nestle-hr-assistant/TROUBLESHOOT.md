# TROUBLESHOOT: Common Issues

## "No PDF files found"
Put your PDFs in a folder named `documents` in the same directory as the script. Check the path: `DOCUMENTS_PATH = "documents"`.

## "OpenAI API key not found"
Create a `.env` file with `OPENAI_API_KEY=sk-...`. Or run `export OPENAI_API_KEY=sk-...` in the terminal before starting.

## "ModuleNotFoundError: langchain"
Run `pip install -r requirements.txt`. You need langchain, langchain-openai, langchain-community, faiss-cpu, pypdf, gradio.

## Slow first run
Embedding all chunks takes time. After the first run, you could save the vector store and load it next time (advanced).

## Wrong or vague answers
Try increasing `k` in search_kwargs: `{"k": 5}` gets more chunks. Or make chunks smaller: `chunk_size=500`.
