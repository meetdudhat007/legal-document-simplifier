# Legal Document Simplifier

An AI-powered web application that simplifies complex legal documents into easy-to-understand language, provides summaries, highlights key clauses, and enables document-based Q&A using NLP techniques.

![Project Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![React](https://img.shields.io/badge/react-19.x-blue)
![FastAPI](https://img.shields.io/badge/fastapi-0.100+-green)

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [License](#license)

## ✨ Features

- **Document Upload**: Upload legal documents (PDF, TXT, DOCX) for analysis
- **AI-Powered Simplification**: Converts complex legal language into plain English
- **Smart Summaries**: Generates concise summaries of legal documents
- **Key Clause Detection**: Automatically identifies and highlights important clauses
- **Interactive Q&A**: Ask questions about your uploaded documents and get AI-generated answers
- **Modern UI**: Clean, responsive interface built with React and Tailwind CSS

## 🛠 Tech Stack

### Backend
- **Python 3.10+**
- **FastAPI** - Modern web framework for building APIs
- **Hugging Face Inference API** - AI-powered text processing
- **python-docx** - DOCX file parsing
- **PyPDF2** - PDF file parsing

### Frontend
- **React 19** - UI library
- **Vite** - Build tool
- **Tailwind CSS 4** - Styling
- **Axios** - HTTP client
- **React Dropzone** - File upload component

## 📁 Project Structure

```
Chatbot/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt    # Python dependencies
│   ├── .env                # Environment variables
│   └── services/
│       ├── document_parser.py  # Document text extraction
│       └── llm_service.py      # AI processing logic
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chatbot.jsx      # Q&A chat component
│   │   │   ├── ResultsView.jsx  # Analysis results display
│   │   │   └── UploadForm.jsx   # File upload component
│   │   ├── App.jsx             # Main app component
│   │   └── main.jsx            # Entry point
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.10+
- **Hugging Face API Key** (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/meetdudhat007/legal-document-simplifier.git
   cd legal-document-simplifier
   ```

2. **Set up the backend**
   ```bash
   cd backend
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   # Create .env file in backend/ directory
   HUGGINGFACE_API_KEY=your_huggingface_api_key_here
   ```

4. **Set up the frontend**
   ```bash
   cd frontend
   npm install
   ```

### Running the Application

1. **Start the backend server**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. **Start the frontend development server**
   ```bash
   cd frontend
   npm run dev
   ```
   The app will be available at `http://localhost:5173`

## 📖 Usage

1. Open the web application in your browser
2. Click on the upload area or drag and drop a legal document
3. Supported formats: PDF, TXT, DOCX
4. Wait for the AI to analyze the document
5. View the simplified summary and key clauses
6. Use the chat feature to ask specific questions about the document

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/upload` | Upload and analyze a document |
| `POST` | `/api/chat` | Ask questions about the document |

### Example Request

```bash
curl -X POST http://localhost:8000/api/upload \
  -F "file=@document.pdf"
```

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
HUGGINGFACE_API_KEY=your_api_key_here
```

Get your free API key from [Hugging Face](https://huggingface.co/settings/tokens).

## 📄 License

This project is licensed under the MIT License.

---


