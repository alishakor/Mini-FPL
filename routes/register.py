#!/usr/bin/env python3
"""
Handling the registration route
"""
from config import db, app
from forms.signup import RegistrationForm
from flask import render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from models import User


bcrypt = Bcrypt(app)


@app.route('/signup', methods=['GET', 'POST'])
def register():
    """
    code to validate and add user to database
    """
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        # check if the email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already in use. Please use a different email.', 'danger')
            return redirect(url_for('register'))

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # creating a user and saving to database
        user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('USer registered successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
