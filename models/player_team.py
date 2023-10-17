#!/usr/bin/env python3
"""FPL PlayerTeam Relationship module"""
from models.basemodel import BaseModel, db


class PlayerTeamRelationship(BaseModel):
    __tablename__ = "player_team_relationship"
    player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), primary_key=True)
