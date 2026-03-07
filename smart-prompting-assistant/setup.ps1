# Smart AI Prompt Assistant Setup Script for Windows (PowerShell)
# This script checks for Python, creates virtual environment, and sets up the application

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Smart AI Prompt Assistant Setup" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# Function to check if command exists
function Test-CommandExists {
    param($command)
    try {
        if (Get-Command $command -ErrorAction Stop) {
            return $true
        }
    }
    catch {
        return $false
    }
}

# Check if Python is installed
Write-Host "[INFO] Checking for Python..." -ForegroundColor Yellow
if (-not (Test-CommandExists "python")) {
    Write-Host "[ERROR] Python is not installed or not in PATH!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Python is installed" -ForegroundColor Green
$pythonVersion = python --version
Write-Host "     $pythonVersion" -ForegroundColor Gray
Write-Host ""

# Check if virtual environment already exists
if (Test-Path "venv") {
    Write-Host "[INFO] Virtual environment already exists" -ForegroundColor Yellow
    $response = Read-Host "Do you want to recreate it? (y/N)"
    if ($response -eq "y" -or $response -eq "Y") {
        Write-Host "[INFO] Removing existing virtual environment..." -ForegroundColor Yellow
        Remove-Item -Path "venv" -Recurse -Force
    }
    else {
        Write-Host "[INFO] Skipping virtual environment creation" -ForegroundColor Yellow
        $skipVenvCreation = $true
    }
}

# Create virtual environment
if (-not $skipVenvCreation) {
    Write-Host "[INFO] Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv --without-pip
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to create virtual environment" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
    Write-Host ""
}

# Activate virtual environment
Write-Host "[INFO] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to activate virtual environment" -ForegroundColor Red
    Write-Host "You may need to run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
Write-Host ""

# Check if pip is installed
Write-Host "[INFO] Checking for pip..." -ForegroundColor Yellow
try {
    $pipVersion = pip --version 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Pip not found"
    }
    Write-Host "[OK] Pip is already installed" -ForegroundColor Green
}
catch {
    Write-Host "[INFO] Installing pip..." -ForegroundColor Yellow
    if (-not (Test-Path "get-pip.py")) {
        Write-Host "[INFO] Downloading get-pip.py..." -ForegroundColor Yellow
        Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile "get-pip.py"
    }
    python get-pip.py
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to install pip" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "[OK] Pip installed successfully" -ForegroundColor Green
}
Write-Host ""

# Upgrade pip
Write-Host "[INFO] Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip
Write-Host ""

# Install requirements
Write-Host "[INFO] Installing requirements..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to install requirements" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "[OK] All requirements installed" -ForegroundColor Green
Write-Host ""

# Create .env file from .env.example if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "[INFO] Creating .env file from .env.example..." -ForegroundColor Yellow
    if (Test-Path ".env.example") {
        Copy-Item ".env.example" ".env"
        Write-Host "[OK] .env file created successfully" -ForegroundColor Green
        Write-Host "[IMPORTANT] Please edit .env file and add your API keys" -ForegroundColor Yellow
        Write-Host ""
    }
    else {
        Write-Host "[WARNING] .env.example not found, skipping .env creation" -ForegroundColor Yellow
        Write-Host ""
    }
}
else {
    Write-Host "[INFO] .env file already exists, skipping creation" -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Setup completed successfully!" -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Cyan
Write-Host "  1. Edit the .env file and add your Google Gemini API key" -ForegroundColor Yellow
Write-Host "     Get your API key from: https://makersuite.google.com/app/apikey" -ForegroundColor Gray
Write-Host ""
Write-Host "To run the application:" -ForegroundColor Yellow
Write-Host "  1. Activate virtual environment: venv\Scripts\activate" -ForegroundColor Gray
Write-Host "  2. Run the app: python run.py" -ForegroundColor Gray
Write-Host ""
Write-Host "Or simply run: .\start_app.bat" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to exit"
