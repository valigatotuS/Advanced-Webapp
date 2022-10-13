#--- App extensions (avoiding circular imports) ---#

import flask_login
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = flask_login.LoginManager()