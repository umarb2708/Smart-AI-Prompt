@echo off
REM Smart AI Prompt Assistant Setup Script for Windows
REM This script checks for Python, creates virtual environment, and sets up the application

echo ====================================
echo Smart AI Prompt Assistant Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM Check if virtual environment already exists
if exist "venv\" (
    echo [INFO] Virtual environment already exists
    choice /C YN /M "Do you want to recreate it"
    if errorlevel 2 goto skip_venv_creation
    if errorlevel 1 (
        echo [INFO] Removing existing virtual environment...
        rmdir /s /q venv
    )
)

:create_venv
echo [INFO] Creating virtual environment...
python -m venv venv --without-pip
if %errorlevel% neq 0 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment created
echo.

:skip_venv_creation
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment activated
echo.

REM Check if pip is installed in venv
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Installing pip...
    if not exist "get-pip.py" (
        echo [INFO] Downloading get-pip.py...
        powershell -Command "Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py"
    )
    python get-pip.py
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install pip
        pause
        exit /b 1
    )
    echo [OK] Pip installed successfully
    echo.
)

echo [INFO] Upgrading pip...
python -m pip install --upgrade pip
echo.

echo [INFO] Installing requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install requirements
    pause
    exit /b 1
)
echo [OK] All requirements installed
echo.

REM Create .env file from .env.example if it doesn't exist
if not exist ".env" (
    echo [INFO] Creating .env file from .env.example...
    if exist ".env.example" (
        copy ".env.example" ".env" >nul
        echo [OK] .env file created successfully
        echo [IMPORTANT] Please edit .env file and add your API keys
        echo.
    ) else (
        echo [WARNING] .env.example not found, skipping .env creation
        echo.
    )
) else (
    echo [INFO] .env file already exists, skipping creation
    echo.
)

echo ====================================
echo Setup completed successfully!
echo ====================================
echo.
echo NEXT STEPS:
echo   1. Edit the .env file and add your Google Gemini API key
echo      Get your API key from: https://makersuite.google.com/app/apikey
echo.
echo To run the application:
echo   1. Activate virtual environment: venv\Scripts\activate
echo   2. Run the app: python run.py
echo.
echo Or simply run: start_app.bat
echo.
pause
