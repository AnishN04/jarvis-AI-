@echo off
echo ================================================
echo Jarvis AI Assistant - Complete Setup (Gemini)
echo ================================================
echo.

REM Check Python
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)
python --version
echo.

REM Check Node.js
echo [2/4] Checking Node.js installation...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)
node --version
npm --version
echo.

REM Setup Python Backend
echo [3/4] Setting up Python backend...
cd backend
if not exist venv (
    echo Creating Python virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python dependencies
    pause
    exit /b 1
)

echo Creating .env file...
if not exist .env (
    if exist .env.example (
        copy .env.example .env
        echo .env file created. Please edit it and add your Gemini and Pinecone API keys.
    ) else (
        echo PINECONE_API_KEY=your_pinecone_api_key_here > .env
        echo GEMINI_API_KEY=your_gemini_api_key_here >> .env
        echo .env file created. Please edit it and add your Gemini and Pinecone API keys.
    )
) else (
    echo .env file already exists.
)

cd ..
echo.

REM Setup React Frontend
echo [4/4] Setting up React frontend...
cd frontend

echo Installing Node.js dependencies...
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install Node.js dependencies
    pause
    exit /b 1
)

cd ..
echo.

echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Get a Gemini API key from https://aistudio.google.com/
2. Get a Pinecone API key from https://www.pinecone.io/
echo 3. Edit backend\.env and add your API keys
echo 4. Run start.bat to launch the application
echo.
pause
