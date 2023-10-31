#!/usr/bin/env python3
"""
team selectionn from squad
"""
from flask import jsonify, render_template
from models.players import Player
from models.basemodel import app
from routes import pick_bp


@pick_bp.route('/',  methods=['GET', 'POST'], strict_slashes=False)
def index():

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