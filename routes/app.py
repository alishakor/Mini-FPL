#!/usr/bin/env python3
"""
flask app module
"""
from models.basemodel import app
from flask_cors import CORS
from flask import jsonify, Response
from . import auth_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
CORS(app)

@app.errorhandler(404)
def error(error) -> Response:
    """
    404 error handler
    """
    return jsonify({"error": "Not found"})


@app.errorhandler(403)
def forbidden_err(error):
    """403 err handler"""
    return jsonify({"error": "unauthorized"})


if __name__ == "__main__":
    app.run(debug=True)