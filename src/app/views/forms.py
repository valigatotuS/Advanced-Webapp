from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, validators
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    """Sign-in form"""
    email = StringField("email", [DataRequired(message="fill your email out")])
    password = PasswordField("password", [DataRequired(message="fill your password out")])
    # role = SelectField(u'Role', choices=["student", "docent", "admin"])
    submit = SubmitField("Log in")

class RegisterForm(FlaskForm):
    """Sign-up form"""
    firstname = StringField("firstname", [DataRequired()])
    lastname = StringField("lastname", [DataRequired()])
    email = StringField("email", [DataRequired()])
    password = PasswordField("password", [DataRequired()])
    submit = SubmitField("Create account")
    