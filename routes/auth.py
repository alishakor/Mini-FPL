#!/usr/bin/env python3
"""
Handling the registration route
"""
from models.basemodel import app
from routes import auth_bp
from forms import RegistrationForm
from forms import LoginForm
from flask import render_template, redirect, url_for, flash
from models.users import User
from flask_login import LoginManager, login_user, logout_user, login_required
from config import bcrypt


@auth_bp.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already in use. Please use a different email.', 'danger')
        else:
            # Hash the password using generate_password_hash
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            
            # Create a user and save to the database
            user = User(
                username=form.username.data,
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                password=hashed_password)
            
            user.save()
            
            flash('User registered successfully!', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)





@auth_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
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
            user = User.query.filter_by(username=form.email_or_username.data).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # Use the check_password_hash method to verify the password
            login_user(user, remember=True)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('profile'))  # Redirect to a different view after successful login
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html', form=form)



@auth_bp.route('/logout')
@login_required
def logout():
    """
    Log out user and destroy session
    """
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
