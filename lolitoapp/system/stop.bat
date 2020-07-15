@echo off
    for /f "tokens=5" %%a in ('
    	netstat -ano ^| findstr :5000
    ') do if not "%%a"=="0" taskkill /F /PID %%a