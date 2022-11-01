"""Initialize Flask Application."""
import flask
from flask import Flask
from app.extensions import db, bcrypt, login_manager
import app.handlers

def create_app(config):
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config)
    
    with app.app_context():
        login_manager.init_app(app)
        db.init_app(app)
        bcrypt.init_app(app)
        #---web-socket---#
        # socketio = SocketIO(app, async_mode=None)
        # socketio.run(app)
        
        #----------------#
        from app.views import routes
        
        # from app.database import manage_db

    return app