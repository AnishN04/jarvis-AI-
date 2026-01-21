# 🚀 CMD Commands for Jarvis AI Assistant (Hugging Face Version)

## ✅ Prerequisites

You only need **2 things** now (no Ollama required!):

1. **Python 3.8+** - https://www.python.org/downloads/
2. **Node.js 16+** - https://nodejs.org/

## 📝 Complete Setup Commands

### Step 1: Navigate to Project

```cmd
cd c:\Users\anish\OneDrive\Desktop\exam-1\jarvis-assistant
```

### Step 2: Run Setup (Installs Everything)

```cmd
setup.bat
```

**What this does:**
- Creates Python virtual environment
- Installs all Python packages
- Downloads TinyLlama model (~2.2GB) - **First time only!**
- Installs Node.js packages
- Creates `.env` file

**Note**: First run takes 5-10 minutes to download the model.

### Step 3: Add Pinecone API Key

Get your free API key from https://www.pinecone.io/

```cmd
notepad backend\.env
```

Change this line:
```
PINECONE_API_KEY=your_pinecone_api_key_here
```

To:
```
PINECONE_API_KEY=pc-xxxxxxxxxxxxxxxxxxxxx
```

Save and close.

### Step 4: Start the Application

```cmd
start.bat
```

**Two windows will open:**
- Backend (Flask) - http://localhost:5000
- Frontend (React) - http://localhost:3000

Your browser will open automatically!

---

## 🎯 That's It!

**Total commands:**
```cmd
cd c:\Users\anish\OneDrive\Desktop\exam-1\jarvis-assistant
setup.bat
notepad backend\.env
start.bat
```

---

## 🔄 Alternative: Manual Commands

If batch files don't work:

### Backend Setup:
```cmd
cd backend
python -m venv venv
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
echo PINECONE_API_KEY=your_key_here > .env
cd ..
```

### Frontend Setup:
```cmd
cd frontend
npm install
cd ..
```

### Start Backend (Window 1):
```cmd
cd backend
call venv\Scripts\activate.bat
python app.py
```

### Start Frontend (Window 2):
```cmd
cd frontend
npm start
```

---

## ✅ Verification

When backend starts, you should see:

```
🤖 Jarvis AI Assistant Backend
==================================================
LLM Status: ✓ Loaded
Pinecone Status: ✓ Connected
==================================================
```

When frontend opens:
- Green dot showing "Connected"
- Welcome message from Jarvis
- Ready to chat!

---

## 🐛 Troubleshooting

### "Python not found"
```cmd
python --version
```
If error, install Python and check "Add to PATH"

### "Node not found"
```cmd
node --version
```
If error, install Node.js

### Model download fails
- Check internet connection
- Need ~3GB free disk space
- Try again: `setup.bat`

### Port 5000 busy
```cmd
netstat -ano | findstr :5000
```
Close other Flask apps

### Port 3000 busy
```cmd
netstat -ano | findstr :3000
```
Close other React apps

---

## 🎨 What's Different from Ollama Version?

✅ **No Ollama installation required**  
✅ **No `ollama pull` commands**  
✅ **Model downloads automatically**  
✅ **Simpler setup - just Python + Node.js**  
✅ **Uses TinyLlama (1.1B) - fast on CPU**  

---

## 📊 System Requirements

- **RAM**: 4GB minimum, 8GB recommended
- **Disk**: 3GB free space
- **CPU**: Any modern processor (no GPU needed)
- **OS**: Windows 10/11

---

## 🔧 Advanced: Change Model

Edit `backend\llm_handler.py` line 6:

```python
# Default (fast, 1.1B)
def __init__(self, model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"):

# Better quality (2.7B, slower)
def __init__(self, model_name: str = "microsoft/phi-2"):

# Best quality (7B, needs more RAM)
def __init__(self, model_name: str = "meta-llama/Llama-2-7b-chat-hf"):
```

Then restart: `start.bat`

---

**That's all! Much simpler than Ollama! 🎉**
