# CONCEPTS: What You Need to Know

## Pandas
Library for tables (dataframes). groupby, sum, read_csv. Used to compute insights directly.

## RAG on Structured Data
Usually RAG is for documents. Here we turn CSV rows into sentences. Same RAG pipeline—chunk, embed, retrieve—but the source is a spreadsheet.

## Hybrid Approach
Sometimes use RAG (for open questions). Sometimes use code (for summaries). Route based on user intent.
