import os

class config:
    TESTING = False
    DEBUG = True            # showing error prompt in browser 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath("./app/app/database/db.sqlite") #./app/...
    SQLALCHEMY_TRACK_MODIFICATIONS = False