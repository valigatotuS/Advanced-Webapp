"""Initialize Flask Application."""
from flask import Flask

def create_app(config):
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config)

    with app.app_context():
        from app.views import routes

        return app