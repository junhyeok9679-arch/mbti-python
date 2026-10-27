@echo off
call "%~dp0activate-local.cmd"
if errorlevel 1 goto failed
python -c "import urllib.request; assert urllib.request.urlopen('http://127.0.0.1:8501/_stcore/health',timeout=1).read() == b'ok'" >nul 2>&1
if errorlevel 1 goto run
start "" "http://127.0.0.1:8501/"
exit /b 0
:run
start "" /b "%CONDA_PREFIX%\pythonw.exe" "%~dp0open-local-browser.py"
python -m streamlit run "%~dp0web_app.py" --server.address 127.0.0.1 --server.port 8501 --server.headless true --browser.gatherUsageStats false
:failed
pause
