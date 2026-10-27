"""서버 준비 후 브라우저 열기. 실행용 보조 파일."""
import time
import urllib.request
import webbrowser

for _ in range(60):
    try:
        with urllib.request.urlopen('http://127.0.0.1:8501/_stcore/health', timeout=1) as response:
            if response.read() == b'ok':
                webbrowser.open('http://127.0.0.1:8501/')
                break
    except OSError:
        pass
    time.sleep(0.5)
