#!/usr/bin/env python3
"""
user login handling
"""
from app import app
from models import User
from flask import render_template, flash, redirect, url_for, request
from flask_login import LoginManager, login_user
from forms.signin import LoginForm

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """Retrieve the user using the user id."""
    return User.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    form = LoginForm()  # Use your LoginForm class

    if form.validate_on_submit():
        # Query the database to find the user by username or email
        input_value = form.email_or_username.data
        password = form.password.data

        # Determine if the input is an email or username
        is_email = '@' in input_value
        if is_email:
            # Query the database to find the user by email
            user = User.query.filter_by(email=input_value).first()
        else:
            # Query the database to find the user by username
            user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            # Use the check_password method to verify the password
            login_user(user, remember=True)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('profile'))  # Redirect to a different view after successful login
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html', form=form)
