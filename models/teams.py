#!/usr/bin/env python3
"""FPL Teams created by users"""
from models.basemodel import BaseModel, db


class FPLTeam(BaseModel):
    __tablename__ = "teams"
    name = db.Column(db.String(128), unique=True, nullable=False)
    player_id = db.Column(db.String(128), db.ForeignKey('players.id'), primary_key=True)
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'), nullable=False, unique=True)
    points = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Numeric(precision=3, scale=1), nullable=False)
    player = db.relationship('Player', backref="teams", lazy=True)
    # Relationship: Teams can have fixtures as home team
    home_fixtures = db.relationship('Fixtures', foreign_keys='Fixtures.home_team_id', backref='home_team')
    # Relationship: Teams can have fixtures as away team
    away_fixtures = db.relationship('Fixtures', foreign_keys='Fixtures.away_team_id', backref='away_team')


