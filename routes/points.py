#!/usr/bin/env python3
"""
routes for point.html
"""
from db_script import get_players_info_from_team
from routes import point_bp
from models.teams import FPLTeam
from models.players import Player
from flask import render_template
from flask_login import current_user, login_required


@point_bp.route('/points', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def index():
    user_id = current_user.id
    user_team = FPLTeam.query.filter_by(user_id=user_id).first()

    starting_player_ids = [player.id for player in user_team.starting_players]
    bench_player_ids = [player.id for player in user_team.bench_players]

    starting_footballers = []
    bench_footballers = []
    players = Player.query.all()

    for player in players:
        if player.id in starting_player_ids:
            starting_footballers.append({
                "name": player.name,
                "image": player.image,
                "points": player.points_per_game
            })
        if player.id in bench_player_ids:
            bench_footballers.append({
                "name": player.name,
                "image": player.image,
                "points": player.points_per_game
            })





    return render_template('points.html', starting_footballers=starting_footballers, bench_footballers=bench_footballers, team=user_team)
