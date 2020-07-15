cd "%~dp0\.." & ^
env\Scripts\activate & ^
start "" /B view.py & ^
start "" /B flask run