# Jarvis - Personal AI Assistant (Gemini Version)

A personal AI assistant powered by **Google Gemini API** with Pinecone vector database for knowledge retrieval and a modern React chatbot UI.

## 🎯 Features

- **Gemini LLM**: Uses Google's Gemini Pro API (fast and intelligent)
- **Vector Database**: Pinecone for semantic search and knowledge retrieval
- **Modern React UI**: Beautiful, responsive chatbot interface with dark theme
- **Context-Aware**: Retrieves relevant knowledge to provide better answers
- **Streamlined**: No local model downloads or heavy disk usage

## 📋 Prerequisites

Before you begin, install the following:

1. **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
   - ⚠️ **Important**: Check "Add Python to PATH" during installation

2. **Node.js 16+** - [Download Node.js](https://nodejs.org/)
   - Includes npm package manager

3. **Gemini API Key** - [Get it free from Google AI Studio](https://aistudio.google.com/)

4. **Pinecone API Key** - [Sign up for free at Pinecone](https://www.pinecone.io/)

## 🚀 Quick Start

### Step 1: Run Setup

Open **Command Prompt (cmd)** and navigate to the project:

```cmd
cd c:\Users\anish\OneDrive\Desktop\exam-1\jarvis-assistant
setup.bat
```

This will:
- Create Python virtual environment
- Install Python and Node.js dependencies
- Create `.env` file template

### Step 2: Configure API Keys

Edit `backend\.env` and add your keys:

```
PINECONE_API_KEY=your_pinecone_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### Step 3: Start the Application

```cmd
start.bat
```

This will:
- Start the Flask backend on http://localhost:5000
- Start the React frontend on http://localhost:3000
- Automatically open your browser

## 📁 Project Structure

```
jarvis-assistant/
├── backend/
│   ├── app.py              # Flask server
│   ├── llm_handler.py      # Gemini integration
│   ├── vector_store.py     # Pinecone / Gemini embeddings
│   ├── requirements.txt    # Python dependencies
│   └── .env               # API keys
├── frontend/               # React app
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatMessage.jsx
│   │   │   ├── ChatInput.jsx
│   │   │   └── StatusIndicator.jsx
│   │   ├── App.jsx
│   │   └── App.css
│   └── package.json
├── setup.bat              # Setup script
├── start.bat              # Launch script
└── README.md              # This file
```

## 📚 Adding Knowledge

You can add documents to the knowledge base via the API:

```python
import requests

documents = ["Information about Jarvis..."]
requests.post('http://localhost:5000/add-knowledge', json={'documents': documents})
```

## 🔧 Manual Setup

### Backend:
```cmd
cd backend
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Frontend:
```cmd
cd frontend
npm install
```

---

**Powered by React, Gemini, and Pinecone**
