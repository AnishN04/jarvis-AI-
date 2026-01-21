# 🚀 CMD Commands for Jarvis AI Assistant (Gemini API)

## ✅ Prerequisites

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
- Installs all Python packages (including Gemini client)
- Installs Node.js packages
- Creates `.env` file

### Step 3: Add API Keys

1. Get **Gemini API Key**: https://aistudio.google.com/
2. Get **Pinecone API Key**: https://www.pinecone.io/

```cmd
notepad backend\.env
```

Add your keys:
```
PINECONE_API_KEY=your_pinecone_key
GEMINI_API_KEY=your_gemini_key
```

Save and close.

### Step 4: Start the Application

```cmd
start.bat
```

**Two windows will open:**
- Backend (Flask) - http://localhost:5000
- Frontend (React) - http://localhost:3000

---

## ✅ Verification

When backend starts, you should see:

```
🤖 Jarvis AI Assistant Backend
==================================================
LLM Status: ✓ Loaded (Gemini)
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

### Port 5000 busy
```cmd
netstat -ano | findstr :5000
```
Close other Flask apps or search for the PID in Task Manager and end it.

### Port 3000 busy
```cmd
netstat -ano | findstr :3000
```
Close other React apps.

---

## 🎨 What's Different?

✅ **Fast Startup**: Instantly connects to Gemini API.
✅ **No Local Storage**: No 2GB+ model files on your disk.
✅ **Higher Quality**: Uses Google's state-of-the-art Gemini Pro.
✅ **Cloud Embeddings**: Uses Gemini for semantic search as well.

---

**Built with ❤️ using React, Gemini, and Pinecone**
