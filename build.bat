@echo off
setlocal

cd /d "%~dp0"

echo.
echo ====== booKeeper Setup  =======
echo.

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    py -m venv .venv
    if errorlevel 1 (
        echo -------ERROR---------
        echo Failed to create virtual environment.
        echo ----------------------
        echo .
        pause 
        exit /b 1
    )
)

echo Installing dependencies...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo -------ERROR---------
    echo Failed to install python package dependencies
    echo Please check the above error.
    echo ----------------------
    echo.
    pause
    exit /b 1

)

if not exist ".env" (
    echo.
    echo === MongoDB Setup ===
    echo.
    echo Get your MongoDB connection string from the link in the repository's README.
    echo.
    
    copy ".env.example" ".env" >nul
    
    echo Opening .env...
    start "" ".env"
    
    echo.
    echo Add your MongoDB connection string to .env.
    echo Save the file, then run build.bat again.
    echo.
    pause
    exit /b 0
)

echo Hey! The Setup completed!!
echo.
echo Starting booKeeper...
echo.

".venv\Scripts\python.exe" run_me.py

pause