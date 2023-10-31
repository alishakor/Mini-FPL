from flask import render_template
from routes import fixtures_bp

import requests

api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"


@fixtures_bp.route('/fixtures', methods=['GET', 'POST'], strict_slashes=False)
def index():
    game_week = "Week 5"
    matches = [
        {"date": "2023-10-15", "home_team": "Team A", "away_team": "Team B"},
        {"date": "2023-10-16", "home_team": "Team C", "away_team": "Team D"},
        # Add more matches as needed
    ]
    return render_template('fixtures.html', game_week=game_week, matches=matches)





# def get_fixtures_data():
#     """ Retrieve the fixtures data for the season
#     """
#     url = "https://fantasy.premierleague.com/api/fixtures/"
#     response = ''
#     while response == '':
#         try:
#             response = requests.get(url)
#         except:
#             time.sleep(5)
#     if response.status_code != 200:
#         raise Exception("Response was code " + str(response.status_code))
#     data = json.loads(response.text)
#     return data