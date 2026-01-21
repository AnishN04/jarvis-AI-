# Jarvis - Personal AI Assistant

A personal AI assistant powered by **Hugging Face Transformers** (TinyLlama) with Pinecone vector database for knowledge retrieval and a modern React chatbot UI.

## 🎯 Features

- **Local LLM**: Uses TinyLlama via Hugging Face Transformers (runs locally, no API costs)
- **Vector Database**: Pinecone for semantic search and knowledge retrieval
- **Modern React UI**: Beautiful, responsive chatbot interface with dark theme
- **Context-Aware**: Retrieves relevant knowledge to provide better answers
- **Component-Based**: Modular React architecture for easy customization
- **No Ollama Required**: Uses Hugging Face Transformers directly

## 📋 Prerequisites

Before you begin, install the following:

1. **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
   - ⚠️ **Important**: Check "Add Python to PATH" during installation

2. **Node.js 16+** - [Download Node.js](https://nodejs.org/)
   - Includes npm package manager

3. **Pinecone Account** - [Sign up for free](https://www.pinecone.io/)
   - Get your API key from the dashboard

## 🚀 Quick Start

### Step 1: Run Setup

Open **Command Prompt (cmd)** and navigate to the project:

```cmd
cd c:\Users\anish\OneDrive\Desktop\exam-1\jarvis-assistant
setup.bat
```

This will:
- Create Python virtual environment
- Install Python dependencies (including TinyLlama model)
- Install Node.js dependencies
- Create `.env` file

**Note**: First run will download the TinyLlama model (~2.2GB). This may take a few minutes.

### Step 2: Configure Pinecone

Edit `backend\.env` and add your Pinecone API key:

```
PINECONE_API_KEY=your_actual_api_key_here
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
│   ├── app.py              # Flask REST API server
│   ├── llm_handler.py      # Hugging Face Transformers integration
│   ├── vector_store.py     # Pinecone vector database
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables
├── frontend/
│   ├── public/
│   │   └── index.html     # HTML template
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatMessage.jsx
│   │   │   ├── ChatInput.jsx
│   │   │   └── StatusIndicator.jsx
│   │   ├── App.jsx        # Main app component
│   │   ├── App.css        # Styling
│   │   ├── index.js       # React entry point
│   │   └── index.css      # Global styles
│   └── package.json       # Node.js dependencies
├── data/
│   └── knowledge_base.txt # Sample knowledge
├── setup.bat              # Setup script
├── start.bat              # Start script
└── README.md              # This file
```

## 💬 Usage

1. Open http://localhost:3000 in your browser
2. Wait for the status indicator to show "Connected" (green dot)
3. Type your message in the input box
4. Press Enter or click the send button
5. Jarvis will respond using the TinyLlama model

## 🔧 Model Information

**Default Model**: TinyLlama/TinyLlama-1.1B-Chat-v1.0
- Size: ~2.2GB
- Parameters: 1.1 Billion
- Fast inference on CPU
- Good for general conversation

**Alternative Models** (edit `backend/llm_handler.py`):
- `microsoft/phi-2` - 2.7B parameters, better quality
- `meta-llama/Llama-2-7b-chat-hf` - 7B parameters, requires HF token

## 📚 Adding Knowledge to the Database

You can add documents to the knowledge base using the API:

```python
import requests

documents = [
    "Your knowledge document 1",
    "Your knowledge document 2"
]

response = requests.post(
    'http://localhost:5000/add-knowledge',
    json={'documents': documents}
)

print(response.json())
```

## 🛠️ Manual Setup (Alternative)

If the batch files don't work, run these commands manually in **cmd**:

### Backend Setup:
```cmd
cd backend
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo PINECONE_API_KEY=your_key_here > .env
```

### Frontend Setup:
```cmd
cd frontend
npm install
```

### Start Backend:
```cmd
cd backend
call venv\Scripts\activate.bat
python app.py
```

### Start Frontend (in a new cmd window):
```cmd
cd frontend
npm start
```

## 🐛 Troubleshooting

### Python not found
- Reinstall Python and check "Add to PATH"
- Restart Command Prompt after installation

### Node.js not found
- Install Node.js from nodejs.org
- Restart Command Prompt after installation

### Model loading errors
- Ensure you have enough disk space (~3GB)
- Check internet connection for first-time download
- Try deleting `~/.cache/huggingface` and rerunning

### Pinecone errors
- Verify your API key in `backend\.env`
- Check you have an active Pinecone account
- Free tier has limitations on index size

### Port already in use
- Backend (5000): Stop other Flask apps
- Frontend (3000): Stop other React apps
- Or restart your computer

## 🎨 Customization

### Change LLM Model
Edit `backend/llm_handler.py`:
```python
llm = LLMHandler(model_name="microsoft/phi-2")  # Use Phi-2 model
```

### Adjust Response Length
Edit `backend/llm_handler.py`:
```python
max_new_tokens=1000  # Increase for longer responses
```

### Modify UI Theme
Edit `frontend/src/App.css` to change colors and styling.

## 📝 API Endpoints

### GET /health
Check server and LLM status

### POST /chat
Send a message and get a response
```json
{
  "message": "Your question here"
}
```

### POST /add-knowledge
Add documents to the knowledge base
```json
{
  "documents": ["doc1", "doc2"]
}
```

## 🔧 Technologies Used

| Component | Technology |
|-----------|-----------|
| Frontend | React 18 |
| Backend | Flask (Python) |
| LLM | TinyLlama via Hugging Face |
| Vector DB | Pinecone |
| Embeddings | sentence-transformers |
| HTTP Client | Axios |

## 📄 License

This project is for educational purposes as part of a programming assignment.

---

**Built with ❤️ using React, TinyLlama, Pinecone, and Flask**
