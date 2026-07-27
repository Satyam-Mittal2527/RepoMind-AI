# 🤖 RepoMind AI

RepoMind AI is an AI-powered GitHub Repository Assistant built using **LangChain**, **Google Gemini**, **FAISS**, and **Streamlit**.

It allows users to analyze any public GitHub repository by asking natural language questions about its architecture, codebase, functionality, and implementation details.

---

## ✨ Features

- 🔗 Clone any public GitHub repository
- 📄 Automatic source code ingestion
- ✂️ Intelligent document chunking
- 🧠 Google Gemini Embeddings
- 📚 FAISS Vector Database
- 🔍 Semantic Code Retrieval
- 💬 Conversational Q&A using LangChain RAG
- 🖥️ Interactive Streamlit Interface

---

## 🛠️ Tech Stack

- Python
- LangChain (LCEL)
- Google Gemini
- FAISS
- Streamlit
- GitPython

---

## 📂 Project Structure

```text
RepoMind/
│
├── streamlit_app.py
│
└── app/
    ├── config.py
    ├── main.py
    ├── rag_chain.py
    ├── runnables.py
    ├── prompt.py
    ├── llm.py
    ├── embeddings.py
    ├── vector_store.py
    │
    └── ingestion/
        ├── github_loader.py
        ├── document_ingestion.py
        └── text_splitter.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/RepoMind.git

cd RepoMind
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 🚀 Run the Application

```bash
streamlit run streamlit_app.py
```

---

## 🧩 How It Works

1. Enter a GitHub repository URL.
2. RepoMind clones the repository using GitPython.
3. Source files are ingested and split into chunks.
4. Chunks are embedded using Google Gemini Embeddings.
5. Embeddings are stored in a FAISS vector database.
6. User questions are answered using a LangChain Retrieval-Augmented Generation (RAG) pipeline.

---

## 🏗️ RAG Pipeline

```
GitHub Repository
        │
        ▼
Git Clone
        │
        ▼
Document Ingestion
        │
        ▼
Text Splitter
        │
        ▼
Gemini Embeddings
        │
        ▼
FAISS Vector Store
        │
        ▼
Retriever
        │
        ▼
Prompt Template
        │
        ▼
Gemini LLM
        │
        ▼
Response
```

---
---

## 🔮 Future Improvements

- Repository summarization
- Multi-repository support
- Source citations in responses
- Conversation memory
- Code explanation mode
- Repository dependency graph
- Docker support
- Deploy on Streamlit Community Cloud

---

## 📄 License

This project is licensed under the MIT License.