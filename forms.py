"""Forms for """

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired, Email


class RegistrationForm(FlaskForm):
    """Form for user registration"""

    username = StringField(
        "Username",
        validators=[InputRequired()])

    password = PasswordField(
        "Password",
        validators=[InputRequired()])

    email = StringField(
        "Email",
        validators=[InputRequired(),Email()])

    first_name = StringField(
        "First_Name",
        validators=[InputRequired()])

    last_name = StringField(
        "Last_Name",
        validators=[InputRequired()])

class LoginForm(FlaskForm):
    """Form for user login."""
    username = StringField(
        "Username",
        validators=[InputRequired()])

    password = PasswordField(
        "Password",
        validators=[InputRequired()])

class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""



