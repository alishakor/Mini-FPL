#!/usr/bin/env python3
from models.basemodel import app, db
from models.players import Player
import requests
players_url = "https://fantasy.premierleague.com/api/bootstrap-static"
batch_size = 100

r = requests.get(players_url)
if r.status_code == 200:
    info = r.json()
    total_players = info["total_players"]
    print(f"Total players: {total_players}")

    for i in range(0, total_players, batch_size):
        batch = info["elements"][i:i+batch_size]
        players = []
        for data in batch:
            # data = info['elements'][i]
            name = data['web_name']
            club = info["teams"][data["team"] - 1]["name"]  # Adjusted to use the correct team index
            element_type_id = data['element_type']
            position = ""
            for element_type in info["element_types"]:
                if element_type["id"] == element_type_id:
                    position = element_type["plural_name_short"]
                    break
            point = data["total_points"]
            cost = data["now_cost"] / 10

            # print(f"Name is {name}")
            # print(f"Club is {club}")
            # print(f"Position is {position}")
            # print(f"Point is {point}")
            # print(f"Cost is {cost}")
            with app.app_context():
                existing_player = Player.query.filter_by(name=name).first()
                if existing_player:
                    existing_player.club = club  # Update the club
                    existing_player.position = position  # Update the position
                    existing_player.point = point  # Update the point
                    existing_player.cost = cost  # Update the cost
                    # You can update any other fields as needed

                    # Commit the changes to the database
                    db.session.commit()
                else:
                    player = Player(
                        name=name,
                        club=club,
                        position=position,
                        point=point,
                        cost=cost,
                        user_id="9c2c1126-00e5-4551-a840-9ecf01aae028"
                    )
                    player.save()
