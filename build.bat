@echo off
setlocal

cd /d "%~dp0"

echo.
echo === booKeeper Setup ===
echo.

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    py -m venv .venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

echo Installing dependencies...
".venv\Scripts\python.exe" -m pip install -r requirements.txt

if not exist ".env" (
    echo.
    echo Creating .env from .env.example...
    copy ".env.example" ".env" >nul
    echo.
    echo IMPORTANT:
    echo Edit .env and add your MongoDB Atlas connection string. 
    echo.
    pause
    exit /b 0
)

echo Yoo it workked less goo!!
echo.
echo Starting booKeeper...
echo.

".venv\Scripts\python.exe" run_me.py

pause