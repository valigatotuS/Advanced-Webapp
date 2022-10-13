def init_db():
	"""Initialize database(s)."""
	from app import create_app,db
	from flask import current_app as app
	from app.database.models import User

	db.create_all()

	
init_db()