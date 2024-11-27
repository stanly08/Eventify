from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, FileField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    date = DateField('Event Date', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Event Photo')
    description = TextAreaField('Event Description', validators=[DataRequired()])
    submit = SubmitField('Add Event')

