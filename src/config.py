import os

class config:
    TESTING = False
    DEBUG = True            # showing error prompt in browser 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath("./app/database/db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False