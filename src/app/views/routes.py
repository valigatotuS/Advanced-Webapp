"""Route declaration."""
from flask import current_app as app
from flask import render_template


@app.route("/")
def home():
    """Landing page route."""
    return render_template('lamp_dashboard.html')
