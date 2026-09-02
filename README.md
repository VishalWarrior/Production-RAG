# Production RAG System

A local, cost-free Retrieval-Augmented Generation (RAG) system built using Ollama, Llama 3, ChromaDB, and Python.

This project demonstrates an enterprise-style RAG pipeline that retrieves relevant information from documents and generates answers using a local LLM.

## Features

* PDF document ingestion
* Text extraction with page metadata
* Document chunking
* Chunk validation
* JSON-based processed chunk storage
* Local embeddings using Ollama
* Persistent vector storage using ChromaDB
* Semantic similarity search
* Top-K document retrieval
* Retrieval relevance guardrail
* Local LLM generation using Llama 3
* Source and page citations
* Interactive command-line interface
* Unsupported question handling
* Fully local setup with no API costs

## Architecture

```text
                PDF Documents
                     │
                     ▼
              PDF Text Extraction
                     │
                     ▼
                  Chunking
                     │
                     ▼
              Chunk Validation
                     │
                     ▼
               Ollama Embeddings
                     │
                     ▼
                  ChromaDB
                     │
                     ▼
User Question ──► Query Embedding
                     │
                     ▼
              Semantic Retrieval
                     │
                     ▼
             Relevance Guardrail
                │           │
           Not Relevant    Relevant
                │           │
                ▼           ▼
             No Answer    Llama 3
                              │
                              ▼
                         Final Answer
                              │
                              ▼
                       Source Citations
```

## Tech Stack

* Python
* Ollama
* Llama 3
* `nomic-embed-text`
* ChromaDB
* LangChain
* PyMuPDF

## Project Structure

```text
production-rag/
│
├── data/
│   ├── raw/
│   │   └── enterprise_employee.pdf
│   │
│   └── processed/
│       └── chunks.json
│
├── src/
│   ├── ingestion/
│   │   └── pdf_loader.py
│   │
│   ├── processing/
│   │   ├── chunk_processor.py
│   │   ├── chunk_storage.py
│   │   └── validator.py
│   │
│   ├── embeddings/
│   │   └── ollama_embeddings.py
│   │
│   ├── vectorstore/
│   │   └── chroma_store.py
│   │
│   ├── retrieval/
│   │   ├── retriever.py
│   │   └── relevance.py
│   │
│   ├── generation/
│   │   ├── prompt_builder.py
│   │   ├── llm.py
│   │   └── citations.py
│   │
│   └── storage/
│       └── json_loader.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/production-rag.git
cd production-rag
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Ollama Setup

Install Ollama and download the required local models:

```bash
ollama pull llama3
```

```bash
ollama pull nomic-embed-text
```

Verify installed models:

```bash
ollama list
```

Expected models:

```text
llama3
nomic-embed-text
```

## Running the Application

```bash
python main.py
```

Example:

```text
============================================================
ENTERPRISE RAG ASSISTANT
Type 'exit' to quit
============================================================

Ask a question: How many annual leave days do employees get?

FINAL ANSWER:

Employees are entitled to 24 working days of annual leave per calendar year.

SOURCES:
- enterprise_employee.pdf — Page 1
```

## How It Works

### 1. Document Ingestion

PDF documents are loaded and text is extracted page by page.

### 2. Chunking

The extracted text is divided into smaller chunks while preserving metadata such as:

* Source document
* Page number
* File path
* Chunk ID
* Chunk index

### 3. Embeddings

Document chunks are converted into vector embeddings using the local Ollama embedding model:

```text
nomic-embed-text
```

### 4. Vector Storage

Embeddings and document metadata are stored in ChromaDB.

### 5. Retrieval

When a user asks a question:

```text
User Question
      ↓
Query Embedding
      ↓
ChromaDB Similarity Search
      ↓
Top-K Relevant Chunks
```

### 6. Relevance Guardrail

Retrieved results are checked using their similarity distance.

If no sufficiently relevant document is found, the system returns:

```text
I don't know based on the provided documents.
```

This prevents unnecessary LLM calls for clearly unsupported questions.

### 7. Answer Generation

Relevant document chunks are passed to the local Llama 3 model with strict instructions to answer only from the retrieved context.

### 8. Source Citations

Source citations are generated directly from retrieved metadata instead of relying on the LLM to generate citations.

Example:

```text
SOURCES:
- enterprise_employee.pdf — Page 1
```

## Example Questions

```text
How many annual leave days do employees get?
```

```text
What is the remote work policy?
```

```text
How long are operational logs retained?
```

```text
What is the CEO's salary?
```

The last question demonstrates unsupported-question handling.

## Current RAG Pipeline

```text
User Query
    ↓
Query Embedding
    ↓
ChromaDB Retrieval
    ↓
Top-K Results
    ↓
Relevance Guardrail
    ↓
Prompt Builder
    ↓
Local Llama 3
    ↓
Final Answer
    +
Source Citations
```

## Future Improvements

The project will be extended with additional production-level RAG capabilities:

* Hybrid search
* Reranking
* Improved relevance scoring
* Query rewriting
* Multi-document ingestion
* Prompt injection protection
* RAG evaluation dataset
* Retrieval evaluation
* Generation evaluation
* Logging and observability
* FastAPI backend
* Docker containerization
* Authentication and authorization
* Role-based document access
* Production deployment

## Cost

This project is designed to run completely locally.

```text
LLM: Ollama / Llama 3
Embeddings: nomic-embed-text
Vector Database: ChromaDB
```

No paid API is required.

## Learning Goal

The goal of this project is to build a production-oriented understanding of RAG systems and independently design enterprise RAG architectures in the future.

## License

This project is currently intended for learning and portfolio purposes.
