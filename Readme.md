# 📚 Simple RAG Chatbot with Gemini 2.5 and LangChain

This project is a simple **Retrieval-Augmented Generation (RAG) chatbot** built using:

- 🧠 **Google Gemini 2.5 Flash**
- 🧱 **LangChain for chaining + document loading**
- 📄 **Chroma for vector storage**
- 🔍 **PDFMiner for parsing PDFs**

It allows users to ask questions about a PDF and get accurate, source-grounded answers. Ideal for use cases like analyzing novels, academic papers, or course notes. 

This project currently loads and processes one PDF file a book i read recently "The Death of Vivek Oji" for simplicity and experimentation purposes.
Did this as part of a learning project to understand how Retrieval-Augmented Generation (RAG) actually works with LangChain and Gemini. This made it easier for me to test, debug, and build foundational knowledge.

---

## ✨ Features

- ✅ Loads a PDF and splits it into retrievable chunks
- ✅ Uses Gemini embeddings and language model for Q&A
- ✅ Returns answer + source context for transparency
- ✅ Runs locally from your terminal
- ✅ Easily extendable for multiple PDFs or API deployment

---

## 📂 Project Structure

```bash
.
├── the_death_of_vivek_oji.pdf    # Your input PDF
├── rag.py                        # Main Python file
├── requirements.txt              # Python dependencies
└── .env                          # Your API keys
