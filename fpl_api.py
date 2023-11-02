#!/usr/bin/env python3
from models.basemodel import app
from models.players import Player
import requests
players_url = "https://fantasy.premierleague.com/api/bootstrap-static"

r = requests.get(players_url)
if r.status_code == 200:
    info = r.json()
    # total_players = info["total_players"]
    # print(f"Total players: {total_players}")

    for i in range(0, 8):
        data = info['elements'][i]
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
        gameweek_point = data['event_points']

        print(f"Name is {name}")
        print(f"Club is {club}")
        print(f"Position is {position}")
        print(f"Total Point is {point}")
        print(f"Cost is {cost}")
        print(f"Game point is {gameweek_point}")
        # with app.app_context():
        #     player = Player(
        #         name=name,
        #         club=club,
        #         position=position,
        #         point=point,
        #         cost=cost,
        #         user_id="9c2c1126-00e5-4551-a840-9ecf01aae028"
        #     )
        #     player.save()
