#!/usr/bin/env python3
from models.basemodel import app
from models.players import Player
import requests
from datetime import datetime
from pytz import timezone

players_url = "https://fantasy.premierleague.com/api/bootstrap-static"
players_url = f"https://fantasy.premierleague.com/api/fixtures?future=1"
res = requests.get(players_url)
out = res.json()

# my_set = set()  # Define a set to store unique dates

for i in range(0, 12):
    data = out[i].get('kickoff_time')
    # print(data)


# Convert the time to the UK (GMT) time zone

# utc_time = datetime.strptime("2023-11-04T12:30:00Z", "%Y-%m-%dT%H:%M:%SZ")
    utc_time = datetime.strptime(data, "%Y-%m-%dT%H:%M:%SZ")
    wat_tz = timezone('Africa/Lagos')  # 'Europe/London' is the time zone for the UK
    wat_time = utc_time.astimezone(wat_tz)

    print(data)
    print(wat_time)
# 2023-11-04T12:30:00Z
# r = requests.get(players_url)
# if r.status_code == 200:
#     info = r.json()
#     # total_players = info["total_players"]
#     # print(f"Total players: {total_players}")
#
#     for i in range(0, 8):
#         data = info['elements'][i]
#         name = data['web_name']
#         club = info["teams"][data["team"] - 1]["name"]  # Adjusted to use the correct team index
#         element_type_id = data['element_type']
#         position = ""
#         for element_type in info["element_types"]:
#             if element_type["id"] == element_type_id:
#                 position = element_type["plural_name_short"]
#                 break
#         point = data["total_points"]
#         cost = data["now_cost"] / 10
#         gameweek_point = data['event_points']
#
#
#         print(f"Name is {name}")
#         print(f"Club is {club}")
#         print(f"Position is {position}")
#         print(f"Total Point is {point}")
#         print(f"Cost is {cost}")
#         print(f"Game point is {gameweek_point}")
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
