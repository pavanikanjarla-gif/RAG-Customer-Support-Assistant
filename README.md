# 🚀 RAG-Based Customer Support Assistant

## 📌 Overview
This project implements a Retrieval-Augmented Generation (RAG) system to answer user queries from PDF documents using AI.

## ❗ Problem Statement
Searching large documents manually is time-consuming and inefficient.

## 💡 Solution
This system allows users to ask questions and get accurate answers using:
- Document chunking
- Embeddings
- Vector search
- LLM-based response generation

---

## 🧠 Architecture
User Query → Retriever → Relevant Chunks → LLM → Answer → HITL

---

## ⚙️ Tech Stack
- Python
- LangChain
- ChromaDB
- HuggingFace Embeddings
- LangGraph
- LLM (Groq / LLaMA)

---

## 🔄 Workflow
1. PDF is loaded
2. Text is split into chunks
3. Embeddings are generated
4. Stored in ChromaDB
5. User query is processed
6. Relevant chunks retrieved
7. LLM generates answer
8. HITL triggered if needed

---

## 📂 Documents
- HLD.pdf
- LLD.pdf
- Technical Documentation.pdf

---

## 🎥 Demo Video
https://drive.google.com/file/d/193aacEDiAFBU4g7rFxF5gPkPzxK8hBgY/view?usp=sharing

---

## 🎯 Features
✔ Context-based answers  
✔ Efficient retrieval  
✔ Scalable architecture  
✔ Human-in-the-loop support  

---

## 🚧 Future Improvements
- Multi-document support  
- UI development  
- Deployment  

---

## 🙌 Author
K.Pavani
