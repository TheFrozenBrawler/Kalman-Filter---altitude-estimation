@echo off

:: Check if Python is installed
where python >nul 2>nul
if errorlevel 1 (
    echo Python not found. Make sure Python is installed and added to your PATH.
    exit /b 1
)

:: Check if Python version is 3.11 or higher
for /f "tokens=2 delims=." %%i in ('python --version 2>&1') do (
    if %%i LSS 11 (
        echo Python version 3.11 or higher is required.
        exit /b 1
    )
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo Setup done! Use '.\run.bat' to run the program.