#!/usr/bin/env python3
"""
Retrieving players from database
"""
from flask import jsonify, render_template
from models.players import Player
from models.basemodel import app
from routes import create_bp


@create_bp.route('/',  methods=['GET', 'POST'], strict_slashes=False)
def index():
    return render_template('create-team.html')

@create_bp.route('/get_player_data')
def get_player_data():
    players = Player.query.all()
    player_data = [{
        'id': player.id,
        'name': player.name,
        'position': player.position,
        'price': player.price
    } for player in players]
    return jsonify(player_data)
