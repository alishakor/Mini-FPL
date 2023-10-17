#!/usr/bin/env python3
"""
A user logout module
"""
from app import app
from flask import flash, redirect, url_for
from flask_login import login_required, logout_user


@app.route('/logout')
@login_required
def logout():
    """
    Log out user and destroy session
    """
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))
