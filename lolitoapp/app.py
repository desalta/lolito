from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from helper import database

app = Flask(__name__)
db = SQLAlchemy()

app.config.from_object(config.miconfig())
db.init_app(app)

import routes

with app.app_context():
    db.create_all()