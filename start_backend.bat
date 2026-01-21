@echo off
echo ================================================
echo Starting Jarvis AI Assistant Backend
echo ================================================
echo.

cd backend

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting Flask server...
python app.py

pause
