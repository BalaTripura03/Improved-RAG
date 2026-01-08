📘 Improved Retrieval Strategy for RAG using FAISS and Semantic Embeddings
📌 Project Overview

This project implements an improved retrieval strategy for a Retrieval-Augmented Generation (RAG) system, focusing on delivering coherent, relevant, and reliable context before response generation.

The system uses:

LLM research papers (PDFs) as the knowledge base

Semantic embeddings for meaning-based retrieval

FAISS vector database for efficient similarity search

The goal is to overcome limitations of traditional keyword-based retrieval, such as incomplete context and loosely related documents, especially in enterprise and regulated environments.

🎯 Problem Statement Addressed

Problem Statement 2:
Improve the retrieval logic in a RAG system so that large language models receive high-quality, contextually relevant evidence, reducing hallucinations and increasing explainability.

🧠 Retrieval Pipeline Architecture

Load research papers in PDF format

Extract and split text into overlapping chunks

Generate semantic embeddings using a lightweight transformer model

Store embeddings in a FAISS vector database

Retrieve top-k relevant chunks for a user query

This pipeline improves retrieval quality before any language model generates a response.

📂 Project Structure
rag_task/
│── main.py                  # Main retrieval pipeline
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
│
└── data/
    └── papers/              # Folder containing LLM research PDFs
        ├── paper1.pdf
        ├── paper2.pdf

⚙️ Technologies Used

Python 3.10+

LangChain

FAISS (CPU)

Sentence-Transformers

PyPDF

Torch

📦 Installation & Setup
1️⃣ Clone or Download the Project
git clone <your-repository-link>
cd rag_task

2️⃣ Create a Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

📄 Prepare the Corpus

Place top 10 LLM research papers (PDFs) inside:

data/papers/


Example:

data/papers/llm_survey.pdf
data/papers/rag_paper.pdf

▶️ How to Run the Project

Run the main pipeline:

python main.py

Expected Console Flow
📄 Loading PDF files...
➡ Loading: paper1.pdf
➡ Loading: paper2.pdf

📘 Total pages loaded: 124

✂️ Splitting into chunks...
✅ Total chunks created: 356

🔢 Loading embedding model...

🗄️ Building FAISS vector database...
Processing batch 1/4...
Processing batch 2/4...
✅ FAISS index built successfully!

❓ Please enter your query:


Enter a query, for example:

What are the limitations of large language models?

📊 Output

The system returns the top-k most relevant text chunks from the research papers based on semantic similarity.

These retrieved chunks can be directly passed to an LLM for grounded response generation, making this a reliable RAG retrieval layer.

🚧 Challenges Faced & Optimizations

Issue: FAISS indexing appeared to hang during execution.
Root Causes:

Heavy embedding models

First-time model downloads

Large number of chunks on CPU

Fixes Implemented:

Switched to lightweight all-MiniLM-L6-v2 embedding model

Added progress logs

Used batch processing for FAISS indexing

This ensured stable, fast, and reproducible retrieval.

✅ Key Benefits

Semantic (meaning-based) retrieval instead of keyword matching

Reduced irrelevant or fragmented context

Improved reliability and explainability

Enterprise-ready retrieval design

📌 Notes

This project focuses on the retrieval stage of RAG, which is the primary source of hallucinations if done poorly.

Language model generation can be added later on top of this retrieval layer.

🙏 Acknowledgment

Thank you for reviewing this project.
This implementation demonstrates how improving retrieval quality significantly enhances the reliability of RAG-based AI systems.