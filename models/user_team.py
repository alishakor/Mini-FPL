#!/usr/bin/env python3
"""FPL UserTeam Realtionship module"""
from models.basemodel import BaseModel, db


class UserTeamRelationship(BaseModel):
    __tablename__ = "user_team_relationship"
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), primary_key=True)
