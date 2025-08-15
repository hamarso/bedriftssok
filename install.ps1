# Install script for Enhetsregisteret app
Write-Host "🔧 Installing dependencies for Enhetsregisteret app..." -ForegroundColor Green

# Check if Python is available
$pythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
} else {
    Write-Host "❌ Python not found! Please install Python first:" -ForegroundColor Red
    Write-Host "   Visit: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "   Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Found Python: $pythonCmd" -ForegroundColor Green

# Create virtual environment if it doesn't exist
if (-not (Test-Path ".venv")) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Blue
    & $pythonCmd -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to create virtual environment" -ForegroundColor Red
        exit 1
    }
}

# Activate virtual environment and install packages
Write-Host "📥 Installing packages..." -ForegroundColor Blue
$venvPython = ".\.venv\Scripts\python.exe"
if (Test-Path $venvPython) {
    & $venvPython -m pip install --upgrade pip
    & $venvPython -m pip install -r requirements.txt
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Installation completed successfully!" -ForegroundColor Green
        Write-Host "🚀 Run the app with: .\run.ps1" -ForegroundColor Cyan
    } else {
        Write-Host "❌ Installation failed" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "❌ Virtual environment not found" -ForegroundColor Red
    exit 1
}

