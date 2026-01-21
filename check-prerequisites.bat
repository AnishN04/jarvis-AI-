@echo off
echo ================================================
echo Jarvis AI Assistant - Prerequisites Check
echo ================================================
echo.

set ALL_OK=1

REM Check Python
echo [1/3] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo   X Python NOT FOUND
    echo     Install from: https://www.python.org/downloads/
    echo     Make sure to check "Add Python to PATH"
    set ALL_OK=0
) else (
    python --version
    echo   √ Python OK
)
echo.

REM Check Node.js
echo [2/3] Checking Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo   X Node.js NOT FOUND
    echo     Install from: https://nodejs.org/
    set ALL_OK=0
) else (
    node --version
    npm --version
    echo   √ Node.js OK
)
echo.

REM Check Ollama
echo [3/3] Checking Ollama...
ollama --version >nul 2>&1
if errorlevel 1 (
    echo   X Ollama NOT FOUND
    echo     Install from: https://ollama.ai/download
    set ALL_OK=0
) else (
    ollama --version
    echo   √ Ollama OK
    echo.
    echo   Checking LLaMA model...
    ollama list | findstr llama2 >nul 2>&1
    if errorlevel 1 (
        echo   X LLaMA model NOT FOUND
        echo     Run: ollama pull llama2
        set ALL_OK=0
    ) else (
        echo   √ LLaMA model installed
    )
)
echo.

echo ================================================
if %ALL_OK%==1 (
    echo Status: All prerequisites are installed!
    echo.
    echo You can now run: setup.bat
) else (
    echo Status: Some prerequisites are missing.
    echo.
    echo Please install the missing items and run this check again.
)
echo ================================================
echo.
pause
