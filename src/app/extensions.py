#--- App extensions (avoiding circular imports) ---#

import flask_login
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_socketio import SocketIO
from threading import Lock

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = flask_login.LoginManager()
# socketio = SocketIO()
# thread = None
# thread_lock = Lock()
