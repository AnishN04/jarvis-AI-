@echo off
echo ================================================
echo Installing Ollama and LLaMA Model
echo ================================================
echo.

echo Checking if Ollama is installed...
ollama --version
if errorlevel 1 (
    echo.
    echo ERROR: Ollama is not installed!
    echo.
    echo Please download and install Ollama from:
    echo https://ollama.ai/download
    echo.
    echo After installation, run this script again.
    pause
    exit /b 1
)

echo.
echo Ollama is installed!
echo.

echo Pulling LLaMA 2 model (this may take a while, ~3.8GB)...
ollama pull llama2

if errorlevel 1 (
    echo.
    echo ERROR: Failed to pull LLaMA model
    pause
    exit /b 1
)

echo.
echo ================================================
echo LLaMA 2 model installed successfully!
echo ================================================
echo.
echo You can now run the backend server using start_backend.bat
echo.
pause
