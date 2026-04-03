"""
Enabling AI-Powered Business Intelligence for Organizations
InsightForge: RAG on business data + insights + simple visualizations.
"""

import os
import io
import pandas as pd
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import gradio as gr

# Sample business data - in real project use CSV from course
SAMPLE_DATA = """
Date,Product,Revenue,Units
2024-01,Laptop,45000,50
2024-01,Phone,30000,100
2024-02,Laptop,36000,40
2024-02,Phone,24000,80
2024-03,Laptop,54000,60
2024-03,Phone,33000,110
"""


def load_and_process_data():
    """Load business data, create text chunks for RAG."""
    df = pd.read_csv(io.StringIO(SAMPLE_DATA))
    texts = []
    for _, row in df.iterrows():
        text = f"On {row['Date']}, {row['Product']} sold {row['Units']} units for ${row['Revenue']} revenue."
        texts.append(text)
    full_text = " ".join(texts)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents([full_text])
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store, df


def create_qa_chain(vector_store):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever(k=3))


def get_insights(df):
    """Generate simple insights from the data."""
    total_revenue = df["Revenue"].sum()
    best_product = df.groupby("Product")["Revenue"].sum().idxmax()
    trend = "Revenue increased from Jan to Mar." if df["Revenue"].iloc[-1] > df["Revenue"].iloc[0] else "Revenue decreased."
    return f"Total revenue: ${total_revenue}. Best product: {best_product}. Trend: {trend}"


def chat_fn(message, history):
    """Handle question: use RAG for data questions, or return insights summary."""
    if "insight" in message.lower() or "summary" in message.lower():
        return get_insights(df)
    result = qa_chain.invoke({"query": message})
    return result["result"]


# Initialize
vector_store, df = load_and_process_data()
qa_chain = create_qa_chain(vector_store)

demo = gr.ChatInterface(fn=chat_fn, title="InsightForge", description="Ask about business data or request insights.")

if __name__ == "__main__":
    demo.launch()
