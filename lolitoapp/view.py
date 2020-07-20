import webview
import subprocess

window = webview.create_window('Lolito', 'http://localhost:5000',width=910, height=930)
webview.start()
subprocess.call([r'system\stop.bat'])