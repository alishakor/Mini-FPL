#!/usr/bin env python3
"""
A user registration module
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    """
    A class for registration of users
    """
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField(
        'Email Address', validators=[DataRequired(), Length(min=6, max=35)])
    first_name = StringField(
        'First Name', validators=[DataRequired(), Length(min=3, max=25)])
    last_name = StringField(
        'Last Name', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField(
        'Password',
        validators=[DataRequired(),
                    EqualTo('confirm',
                    message='Password must match')])
    confirm = PasswordField('Confirm Password')
    accept_tos = BooleanField('I accept the TOS', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email_or_username = StringField(
        'Email or Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')