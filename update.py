import requests
import time
from models.players import Player
from models.basemodel import db, app

def get_updated_data():
    # Make a GET request to the API to fetch updated player data
    players_url = "https://fantasy.premierleague.com/api/bootstrap-static"
    r = requests.get(players_url)

    if r.status_code == 200:
        info = r.json()
        updated_data = info['elements']

        # Process and return the updated data
        return updated_data

    return []  # Return an empty list if there was an issue fetching the data


# Pseudo-code for updating player data at an interval


while True:
    # Fetch updated player data from the API
    updated_data = get_updated_data()  # Implement this function

    # Update the database with the new 'points' and 'cost' values
    with app.app_context():
        for player_data in updated_data:
            player = Player.query.filter_by(name=player_data['name']).first()
            if player:
                player.point = player_data['total_points']
                player.cost = player_data['now_cost'] / 10
                db.session.commit()

    # Sleep for a specified interval before the next update
    time.sleep(3600)  # Update every hour (adjust as needed)
