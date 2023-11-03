#!/usr/bin/env python3
"""
flask app module
"""
from flask_cors import CORS
from flask import jsonify, Response
from routes import *
from config import app, db
from flask_login import LoginManager
from flask_migrate import Migrate
app.register_blueprint(auth_bp)
app.register_blueprint(players_bp)
app.register_blueprint(fixtures_bp)
app.register_blueprint(create_bp)
app.register_blueprint(pick_bp)
app.register_blueprint(point_bp)
app.register_blueprint(league_bp)
migrate = Migrate(app, db)
CORS(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """Retrieve the user using the user id."""
    return User.query.get(user_id)


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
