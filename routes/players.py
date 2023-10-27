#!/usr/bin/env python3
"""
Fetching player's data
"""
import requests
from flask import render_template
from routes import players_bp

import requests

api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"


@players_bp.route('/', methods=['GET', 'POST'], strict_slashes=False)
def player_data():
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        data = response.json()

        # Extract player data, events data, and teams data
        player_data = data['elements']
        events = data['events']
        teams = data['teams']
        element_types = data['element_types']

        # Sort the player_data list by total_points in descending order
        player_data = sorted(player_data, key=lambda x: x['total_points'], reverse=True)

        return render_template('players.html', player_data=player_data, events=events, teams=teams, element_types=element_types)

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"