#!/usr/bin/env python3
"""
Handling the status route
"""
from models.basemodel import app
from flask import render_template
from flask_login import current_user, login_required


@app.route('/status', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def status():
    username = current_user.username
    return render_template('status.html', username=username)
