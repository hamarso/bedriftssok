# Run script for Enhetsregisteret app
Write-Host "🚀 Starting Enhetsregisteret app..." -ForegroundColor Green

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "❌ Virtual environment not found! Please run install.ps1 first" -ForegroundColor Red
    exit 1
}

# Check if Streamlit is installed
$venvPython = ".\.venv\Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
    Write-Host "❌ Python not found in virtual environment" -ForegroundColor Red
    exit 1
}

# Check if streamlit is installed
$streamlitCheck = & $venvPython -c "import streamlit; print('OK')" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Streamlit not installed! Please run install.ps1 first" -ForegroundColor Red
    exit 1
}

# Start the app
Write-Host "🌐 Starting Streamlit app..." -ForegroundColor Blue
Write-Host "📱 The app will open in your browser shortly..." -ForegroundColor Cyan
Write-Host "🔄 Press Ctrl+C to stop the app" -ForegroundColor Yellow

& $venvPython -m streamlit run app.py

