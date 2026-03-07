@echo off
REM Quick start script for Smart AI Prompt Assistant

echo Starting Smart AI Prompt Assistant...
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo [ERROR] Virtual environment not found!
    echo Please run setup.bat first to set up the environment.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if activation was successful
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)

echo [OK] Virtual environment activated
echo.

REM Run the application
echo [INFO] Starting Flask application...
echo [INFO] Application will be available at http://127.0.0.1:5000
echo [INFO] Press Ctrl+C to stop the server
echo.
python run.py

REM Keep window open if there's an error
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Application exited with an error
    pause
)
