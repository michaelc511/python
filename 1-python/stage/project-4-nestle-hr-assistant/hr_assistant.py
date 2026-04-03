"""
Crafting an AI-Powered HR Assistant: A Use Case for Nestle's HR Policy Documents
Chatbot that answers questions using PDF content. Uses RAG (Retrieval-Augmented Generation).
"""

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import gradio as gr

# Load PDFs from a folder. Put your Nestle HR PDFs in ./documents/
DOCUMENTS_PATH = "documents"


def load_and_index_documents():
    """Load PDFs, split into chunks, create vector store."""
    if not os.path.exists(DOCUMENTS_PATH):
        os.makedirs(DOCUMENTS_PATH)
        print(f"Created {DOCUMENTS_PATH}/ - Add your Nestle HR PDF files there.")
        return None

    documents = []
    for filename in os.listdir(DOCUMENTS_PATH):
        if filename.endswith(".pdf"):
            path = os.path.join(DOCUMENTS_PATH, filename)
            loader = PyPDFLoader(path)
            docs = loader.load()
            documents.extend(docs)

    if not documents:
        print("No PDF files found in documents/.")
        return None

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store


def create_qa_chain(vector_store):
    """Create a chain that retrieves relevant chunks and answers the question."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
    )
    return qa_chain


def chatbot_response(message, history):
    """Gradio chat function. Takes user message, returns AI reply."""
    if qa_chain is None:
        return "Please add PDF files to the 'documents' folder and restart."
    result = qa_chain.invoke({"query": message})
    return result["result"]


# Build the vector store and chain when the script starts
vector_store = load_and_index_documents()
qa_chain = create_qa_chain(vector_store) if vector_store else None

# Gradio interface
demo = gr.ChatInterface(
    fn=chatbot_response,
    title="Nestle HR Assistant",
    description="Ask questions about Nestle HR policies. Answers are based on the PDF documents you added.",
)

if __name__ == "__main__":
    demo.launch()
