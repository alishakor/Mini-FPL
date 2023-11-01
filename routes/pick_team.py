#!/usr/bin/env python3
"""
team selection from squad
"""
import random
from flask import jsonify, render_template
from models.teams import FPLTeam
from models.basemodel import app
from routes import pick_bp
import requests


api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"


@pick_bp.route('/my_team',  methods=['GET', 'POST'], strict_slashes=False)
@login_required
def index():
    """Select your fpl team"""
    return render_template('pick-team.html')

@pick_bp.route('/get_team_data', methods=['GET', 'POST'], strict_slashes=False)
def get_team_data():
    team = FPLTeam.query.all()
    response = requests.get(api_url)
    data = response.json()

    player_data = data['elements']
    events = data['events']
    clubs = data['teams']
    element_types = data['element_types']

    # Separate players by position
    goalkeepers = [player for player in team if player.position == 'GKP']
    defenders = [player for player in team if player.position == 'DEF']
    midfielders = [player for player in team if player.position == 'MiD']
    strikers = [player for player in team if player.position == 'FWD']

     # Randomly select 1 goalkeeper, 4 defenders, 4 midfielders, and 2 strikers
    starting_11 = [random.choice(goalkeepers)]
    starting_11 += random.sample(defenders, 4)
    starting_11 += random.sample(midfielders, 4)
    starting_11 += random.sample(strikers, 2)

    # Mark the selected players as part of the starting 11 in the database
    for player in starting_11:
        player.starting_11 = True

    # Mark the remaining players as substitutes in the database
    for player in team:
        if player not in starting_11:
            player.starting_11 = False
    
    # Organize starting 11 by position
    starting_goalkeepers = [player for player in starting_11 if player.position == 'GKP']
    starting_defenders = [player for player in starting_11 if player.position == 'DEF']
    starting_midfielders = [player for player in starting_11 if player.position == 'MID']
    starting_strikers = [player for player in starting_11 if player.position == 'FWD']


    return render_template(
        'generated-team.html',
        starting_goalkeepers=starting_goalkeepers,
        starting_defenders=starting_defenders,
        starting_midfielders=starting_midfielders,
        starting_strikers=starting_strikers,
        substitutes=team
    )
