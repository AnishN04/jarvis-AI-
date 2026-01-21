@echo off
echo ================================================
echo Starting Jarvis AI Assistant
echo ================================================
echo.
echo This will start both the backend and frontend servers.
echo.
echo Backend: http://localhost:5000
echo Frontend: http://localhost:3000
echo.
echo Press Ctrl+C in each window to stop the servers.
echo.
pause

REM Start backend in new window
echo Starting backend server...
start "Jarvis Backend" cmd /k "cd backend && call venv\Scripts\activate.bat && python app.py"

REM Wait a moment for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend in new window
echo Starting frontend server...
start "Jarvis Frontend" cmd /k "cd frontend && npm start"

echo.
echo ================================================
echo Both servers are starting...
echo ================================================
echo.
echo Backend will run at: http://localhost:5000
echo Frontend will open at: http://localhost:3000
echo.
echo Close the terminal windows to stop the servers.
echo.
