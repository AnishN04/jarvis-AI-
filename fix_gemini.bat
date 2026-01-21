@echo off
echo ================================================
echo Jarvis - Gemini Library Fix & Cleanup
echo ================================================
echo.

echo [1/3] Deleting legacy files...
if exist install_ollama.bat del /f /q install_ollama.bat
if exist QUICKSTART.md del /f /q QUICKSTART.md
if exist start_backend.bat del /f /q start_backend.bat
if exist check-prerequisites.bat del /f /q check-prerequisites.bat
echo ✓ Cleanup complete.

echo.
echo [2/3] Upgrading Google Generative AI library...
cd backend
call venv\Scripts\activate.bat
pip install --upgrade google-generativeai
if errorlevel 1 (
    echo ✗ Error: Failed to upgrade library. Make sure you are connected to the internet.
    pause
    exit /b 1
)
echo ✓ Library upgraded successfully.

echo.
echo [3/3] Verifying model availability...
python -c "import google.generativeai as genai; import os; from dotenv import load_dotenv; load_dotenv(); genai.configure(api_key=os.getenv('GEMINI_API_KEY')); print('Available models:'); [print(m.name) for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]"
echo.
echo ================================================
echo Done! Please restart your backend (python app.py)
echo ================================================
pause
