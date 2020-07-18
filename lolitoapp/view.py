import webview
import subprocess

window = webview.create_window('Lolito', 'http://localhost:5000',width=800, height=800)
webview.start()
subprocess.call([r'system\stop.bat'])