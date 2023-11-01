#!/usr/bin/env python3
"""
team selection from squad
"""
from flask import jsonify, render_template
from models.players import Player
from models.basemodel import app
from routes import pick_bp
from flask_login import login_required


@pick_bp.route('/my_team',  methods=['GET', 'POST'], strict_slashes=False)
@login_required
def index():
    """Select your fpl team"""
    return render_template('pick-team.html')

@pick_bp.route('/get_player_data')
def get_player_data():
    Team = Team.query.all()
    player_data = [{
        'id': player.id,
        'name': player.name,
        'position': player.position,
        'price': player.price
    } for player in players]
    return jsonify(player_data)