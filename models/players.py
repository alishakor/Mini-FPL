#!/usr/bin/env python3
"""players db module"""
from models.basemodel import BaseModel, db


class Player(BaseModel):
    __tablename__ = "players"
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    club = db.Column(db.String(60), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'))
    position = db.Column(db.String(60), nullable=False)
    point = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    team = db.relationship('Team', backref='players')

