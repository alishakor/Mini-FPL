#!/usr/bin/env python3
"""
flask app module
"""
from config import app
from flask_cors import CORS
from flask import jsonify, Response
from . import auth_bp
from . import players_bp
from . import create_bp
from . import pick_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(players_bp, url_prefix='/players')
app.register_blueprint(create_bp, url_prefix='/create-team')
app.register_blueprint(pick_bp, url_prefix='/my-team')
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
