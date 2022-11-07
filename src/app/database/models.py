from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class LampLog(db.Model):
    __tablename__ = "lamplog"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    timestamp = db.Column(db.Integer, primary_key=True)
    lamp_id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
