from flask import Flask  
from flask_sqlalchemy import SQLAlchemy

import config

########################################## BOOTSTRAP

app = Flask(__name__)
db = SQLAlchemy()

import routes

app.config.from_object(config.miconfig())
db.init_app(app)

with app.app_context():
    db.create_all()
 
#import webbrowser
#webbrowser.open_new('http://localhost:5000')