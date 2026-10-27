@echo off
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
call "%USERPROFILE%\miniconda1\condabin\conda.bat" activate myfirstProject
if errorlevel 1 exit /b 1
cd /d "%~dp0"
