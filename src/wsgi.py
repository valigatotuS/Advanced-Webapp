from flask import Flask
from app import create_app
from config import config

app = create_app(config)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=config.DEBUG)