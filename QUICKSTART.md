# 🚀 Quick Start Guide - Jarvis AI Assistant

## Step-by-Step Setup (5 Minutes)

### 1️⃣ Check Prerequisites

Open **Command Prompt (cmd)** and run:

```cmd
cd c:\Users\anish\OneDrive\Desktop\exam-1\jarvis-assistant
check-prerequisites.bat
```

This will check if you have:
- ✅ Python 3.8+
- ✅ Node.js 16+
- ✅ Ollama
- ✅ LLaMA model

### 2️⃣ Install Missing Prerequisites

If anything is missing, install:

| Missing | Download Link | Notes |
|---------|--------------|-------|
| Python | https://www.python.org/downloads/ | ⚠️ Check "Add to PATH" |
| Node.js | https://nodejs.org/ | Includes npm |
| Ollama | https://ollama.ai/download | For LLaMA |

After installing, **restart Command Prompt** and run check again.

### 3️⃣ Install LLaMA Model

```cmd
ollama pull llama2
```

This downloads ~3.8GB. Wait for completion.

### 4️⃣ Run Setup

```cmd
setup.bat
```

This will:
- Create Python virtual environment
- Install Python packages
- Install Node.js packages
- Create `.env` file

### 5️⃣ Add Pinecone API Key

1. Sign up at https://www.pinecone.io/ (free)
2. Get your API key
3. Edit `backend\.env`:
   ```
   PINECONE_API_KEY=your_key_here
   ```

### 6️⃣ Start the Application

```cmd
start.bat
```

Two windows will open:
- **Backend**: http://localhost:5000
- **Frontend**: http://localhost:3000 (opens in browser)

---

## ✅ Verification

When running correctly, you should see:

**Backend Terminal:**
```
🤖 Jarvis AI Assistant Backend
==================================================
Ollama Status: ✓ Connected
Pinecone Status: ✓ Connected
==================================================
```

**Frontend Browser:**
- Green status indicator showing "Connected"
- Welcome message from Jarvis
- Input box ready for messages

---

## 🎯 Testing

1. Type: "What is Jarvis?"
2. Press Enter
3. Wait for response (loading animation shows)
4. Verify you get a response from LLaMA

---

## 🐛 Troubleshooting

### "Python not found"
- Reinstall Python with "Add to PATH" checked
- Restart Command Prompt

### "Node not found"
- Install Node.js from nodejs.org
- Restart Command Prompt

### "Ollama not connecting"
- Open new cmd window
- Run: `ollama serve`
- Keep it running

### "Port already in use"
- Close other Flask/React apps
- Or restart your computer

### "Pinecone error"
- Check API key in `backend\.env`
- Verify it's your actual key (no quotes)

---

## 📝 Commands Reference

| Command | Purpose |
|---------|---------|
| `check-prerequisites.bat` | Verify all software installed |
| `setup.bat` | Install all dependencies |
| `start.bat` | Start both servers |
| `ollama pull llama2` | Download LLaMA model |
| `ollama list` | Check installed models |

---

## 🎨 Features

- **Dark Theme**: Premium purple-pink gradients
- **Real-time Status**: Connection indicator
- **Smooth Animations**: Loading states, message transitions
- **Keyboard Shortcuts**: Enter to send, Shift+Enter for new line
- **Responsive**: Works on desktop and mobile

---

## 📚 More Help

See [README.md](file:///c:/Users/anish/OneDrive/Desktop/exam-1/jarvis-assistant/README.md) for detailed documentation.
