import os

basedir = os.path.abspath(os.path.dirname(__file__))

class miconfig(object):
    SECRET_KEY = 'my_secret_key'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, './database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

