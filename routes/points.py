#!/usr/bin/env python3
"""
routes for point.html
"""
from db_script import get_players_info_from_team
from routes import point_bp
from models.teams import FPLTeam
from flask import render_template

@point_bp.route('/points', methods=['GET', 'POST'], strict_slashes=False)
def index():
    team = FPLTeam.query.all()
    player_info = get_players_info_from_team()
    return render_template('points.html', player_info=player_info, team=team)