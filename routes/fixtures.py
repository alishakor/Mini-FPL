from flask import render_template
from routes import fixtures_bp
from datetime import datetime

import requests

api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"


@fixtures_bp.route('/fixtures', methods=['GET', 'POST'], strict_slashes=False)
def index():
    endpoints = [
        "bootstrap-static",
        "fixtures",
        "element-summary/{element_id}",
        "event/{event_id}/live"
    ]

    # get teams
    teams = {}
    response = requests.get(api_url)
    data = response.json()
    for team in data["teams"]:
        teams[team["id"]] = team

    # get fixtures
    fixture_url = f"https://fantasy.premierleague.com/api/{endpoints[1]}?future=1"
    fixture_response = requests.get(fixture_url)
    fixture_data = fixture_response.json()

    fixtures = {}
    for fixture in fixture_data:
        date = fixture["kickoff_time"]
        time = (date.split('T'))[0].split('-')
        year, month, day = (time[0], time[1], time[2])
        year = int(year)
        month = int(month)
        day = int(day)
        date_obj = datetime(year, month, day)
        date_in_words = date_obj.strftime("%A %d %B %Y")

        fixture["team_a"] = teams[fixture["team_a"]]
        fixture["team_h"] = teams[fixture["team_h"]]

        # check if date_in_words exists in fixtures
        if date_in_words in fixtures:
            fixtures[date_in_words].append({
                "team_a": {
                    "name": fixture["team_a"]["name"],
                    "short_name": fixture["team_a"]["short_name"],
                    "image": "https://resources.premierleague.com/premierleague/badges/70/t" + str(fixture["team_a"]["code"]) + ".png"
                },
                "team_h": {
                    "name": fixture["team_h"]["name"],
                    "short_name": fixture["team_h"]["short_name"],
                    "image": "https://resources.premierleague.com/premierleague/badges/70/t" + str(fixture["team_h"]["code"]) + ".png"
                },
                "time": date.split('T')[1]
            })
        else:
            fixtures[date_in_words] = [{
                "team_a": {
                    "name": fixture["team_a"]["name"],
                    "short_name": fixture["team_a"]["short_name"],
                    "image": "https://resources.premierleague.com/premierleague/badges/70/t" + str(fixture["team_a"]["code"]) + ".png"
                },
                "team_h": {
                    "name": fixture["team_h"]["name"],
                    "short_name": fixture["team_h"]["short_name"],
                    "image": "https://resources.premierleague.com/premierleague/badges/70/t" + str(fixture["team_h"]["code"]) + ".png"
                },
                "time": date.split('T')[1]
            }]
    return render_template('fixtures.html', fixtures=fixtures)


