@echo off
setlocal  

cd /d "@%~dp0"

echo.
echo ====== Updating booKeeper ======
echo.

echo Step 1/2
echo Installing latest version
git pull --ff-only

if errorlevel 1 (
    echo :[
    echo Encountered an error with git....
    echo Pls check the above error 
    echo.
)

echo Step 2/2
echo Updating dependencies
".venv\Scripts\python.exe" -m pip install -r requirements.txt

if errorlevel 1 (
    echo There was an error installing dependencies
    echo please check the pip errors above!
)

echo ======update finished :) =======