"""Forms for """

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired, Email, Length


class RegistrationForm(FlaskForm):
    """Form for user registration"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(max=20)]) #use max/min len validator

    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=100)])

    email = StringField(
        "Email",
        validators=[InputRequired(),Email(), Length(max=50)])

    first_name = StringField(
        "First_Name",
        validators=[InputRequired(), Length(max=30)])

    last_name = StringField(
        "Last_Name",
        validators=[InputRequired(), Length(max=30)])

class LoginForm(FlaskForm):
    """Form for user login."""
    username = StringField(
        "Username",
        validators=[InputRequired(), Length(max=20)])

    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(max=100)])


class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""



