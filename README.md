# Text Summarizer using Transformers (Hugging Face)

This project is a simple and effective text summarization API built using:

- **FastAPI** (for the backend API)
- **Hugging Face Transformers** (for the BART summarizer model)
- **Python** (with PyTorch)
## 🚀 Features

- Accepts raw input text and returns a clean summary.
- Deployed locally with Uvicorn.
- Organized folder structure with modular code.
## 📁 Folder Structure

text_summarizer_project/
└── api/
├── init.py
├── main.py
└── summarizer/
├── init.py
└── summarizer.py
## 🧪 How to Use (Local)

1. Clone the repo  
2. Create a virtual environment:
python -m venv venv
.\venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Run the app:
uvicorn api.main:app --reload
5. Open your browser and go to:
http://127.0.0.1:8000/docs
## 🔗 Live Demo / API Docs

Once running, visit:
http://127.0.0.1:8000/docs

#Author

Prasanna

