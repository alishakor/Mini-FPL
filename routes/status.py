#!/usr/bin/env python3
"""
Handling the status route
"""
from models.basemodel import app
from flask import render_template

@app.route('/status', methods=['GET', 'POST'], strict_slashes=False)
def status():
    return render_template('status.html')