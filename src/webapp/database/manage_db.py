def init_db():
	"""Initialize database(s)."""
	from webapp import create_app,db
	from flask import current_app as app
	from webapp.database.models import User

	db.create_all()

	
init_db()