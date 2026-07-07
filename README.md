# 🏥 Medical RAG Chatbot

A Medical AI Chatbot built using **Retrieval-Augmented Generation (RAG)** that answers questions from medical documents such as doctor notes, lab reports, prescriptions, discharge summaries, and consultation reports.

The chatbot retrieves relevant medical information from a vector database and generates accurate, context-aware responses using Google's Gemini LLM.

---

## 🚀 Features

- 📄 Load medical documents (TXT & PDF)
- ✂️ Recursive document chunking
- 🔍 Semantic search using embeddings
- 🗄️ Chroma Vector Database
- 🤖 Google Gemini LLM
- 💬 Streamlit Chat Interface
- 📚 Source document retrieval
- 🏥 Supports multiple medical document types
- 🔄 Retrieval-Augmented Generation (RAG) pipeline

---

## 🏗️ Project Architecture

```
                Medical Documents
               (TXT / PDF Files)
                        │
                        ▼
              Document Loader
                        │
                        ▼
              Metadata Extraction
                        │
                        ▼
        Recursive Character Splitter
                        │
                        ▼
             HuggingFace Embeddings
                        │
                        ▼
              Chroma Vector Database
                        │
                        ▼
                 Similarity Search
                        │
                        ▼
                 Prompt Template
                        │
                        ▼
                Google Gemini LLM
                        │
                        ▼
                Streamlit Chatbot
```

---

## 📁 Project Structure

```
Medical_chatbot/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   ├── doctor_notes/
│   ├── lab_reports/
│   ├── prescriptions/
│   ├── discharge_summaries/
│   └── consultation_reports/
│
├── src/
│   ├── loader.py
│   ├── metadata.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt.py
│   ├── llm.py
│   └── rag_chain.py
│
└── venv/
```

---

## 🛠️ Tech Stack

- Python 3.11
- LangChain
- Google Gemini API
- Hugging Face Embeddings
- ChromaDB
- Streamlit
- PyPDF
- python-dotenv

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/shoaibrr/Medical-RAG-Chatbot.git
```

```bash
cd Medical-RAG-Chatbot
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Create .env file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

### Run Application

```bash
streamlit run app.py
```

---

## 💬 Example Questions

- What are the symptoms of diabetes?
- Show the patient's lab report.
- What medicines were prescribed?
- Who diagnosed the patient?
- What is the HbA1c value?
- What treatment was recommended?
- Which patient has hypertension?
- Summarize the consultation report.

---

## 📂 Supported Document Types

- Doctor Notes
- Lab Reports
- Prescriptions
- Discharge Summaries
- Consultation Reports

---

## 🔄 RAG Pipeline

1. Load medical documents
2. Extract metadata
3. Split into chunks
4. Generate embeddings
5. Store embeddings in ChromaDB
6. Retrieve relevant chunks
7. Build prompt
8. Generate response using Gemini
9. Display answer in Streamlit

---

## 📈 Future Improvements

- Metadata Filtering
- Conversation Memory
- PDF Upload from UI
- FastAPI Backend
- Docker Support
- RAG Evaluation
- Logging & Monitoring
- Authentication
- Multi-user Support
- Cloud Deployment

---

## 📸 Demo

*(Add screenshots of your Streamlit chatbot here.)*

---

## 👨‍💻 Author

**Shoaib Mohammad**

GitHub: https://github.com/shoaibrr

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.
