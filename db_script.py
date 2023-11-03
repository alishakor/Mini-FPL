#!/usr/bin/env python3
"""
querying from the database
"""
from config import db
from models.players import Player
from models.teams import FPLTeam


def get_players_info_from_team():
    query = db.session.query(Player.name, Player.image, Player.points_per_game). \
        join(FPLTeam, Player.name == FPLTeam.name).all()

    return query