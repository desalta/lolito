#!/bin/bash

cd ../ &&
python3 -m venv env &&
source env/bin/activate &&
pip install flask &&
pip install flask-SQLAlchemy &&
pip install pyautogui &&
pip install pywebview[qt] &&
pip install beautifulsoup4
