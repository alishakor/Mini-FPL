#!/usr/bin/env python3
import requests
from models.players import Player
from config import app

# import sys

endpoints = [
    "bootstrap-static",
    "fixtures",
    "element-summary/{element_id}",
    "event/{event_id}/live"
]

players_url = f"https://fantasy.premierleague.com/api/{endpoints[0]}/"

r = requests.get(players_url)
if r.status_code == 200:
    info = r.json()
    total_players = info["total_players"]
    print(f"Total players: {total_players}")
    # for n in range(3):
    #     player_data = info["elements"][n]
    #     player_id = player_data.get("id")
    #     name = player_data.get("web_name")
    #     point = player_data.get("total_points")
    #     photo = player_data.get("photo")
    #     cost = player_data["now_cost"] / 10.0
    #     print(f"Player_id: {player_id}")
    #     print(f"The player's name: {name}")
    #     print(f"The player's point: {point}")
    #     # print(f"Player's photo: {photo}")
    #     print(f"The player's cost: {cost}")



        # # team index rep the id of the team/club
        # team_index = player_data["team"] - 1
        # team_data = info["teams"][team_index]
        # club_name = team_data.get("name")
        # print(f"The player's club: {club_name}")
        #
        # # element type rep the players position e.g GK:1, DF:2, MF:3, FWD:4
        # element_type_id = player_data.get("element_type")
        # # position = next(item for item in info["element_types"] if item["id"] == element_type_id)
        # position = None
        # for item in info["element_types"]:
        #     if item["id"] == element_type_id:
        #         position = item
        #         break
        # if position:
        #     position_value = position["plural_name"]
        #     print(f"position value: {position_value}")
        # else:
        #     print("Position not found")
        #
        # # Event and Gameweek stat
        # # for n in range(len(info["events"])):
        #
        # event_id = info["events"][0].get("id")
        # game_week = info["events"][event_id - 1].get("name")
        # # print(f"The event id: {event_id}")
        # print(f"The week is: {game_week}")
        #
        # # baller_id = info["elements"][0].get("id")
        # # print(f"Player_id: {baller_id}")
        # team_id = team_index
        # print(f"team_id: {team_id}")
    '''with app.app_context():
        player_stat = Playertest(
                name=name,
                club=club_name,
                position=position_value,
                cost=cost,
                point=point,
                player_id=baller_id,
                team_id=team_id
        )
        player_stat.save()'''
