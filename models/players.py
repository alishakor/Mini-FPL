#!/usr/bin/env python3
"""players db module"""
from models.basemodel import BaseModel, db

association_table = db.Table(
    'team_player_association',
    db.Column('team_id', db.String(128), db.ForeignKey('teams.id')),
    db.Column('player_id', db.String(128), db.ForeignKey('players.id'))
)


class Player(BaseModel):
    __tablename__ = "players"
    name = db.Column(db.String(128), unique=True, nullable=False)
    club = db.Column(db.String(60), nullable=False)
    # team_id = db.Column(db.String(128), db.ForeignKey('teams.id'))
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'))
    position = db.Column(db.String(60), nullable=False)
    point = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    # teams = db.relationship('FPLTeam', db.ForeignKey('FPLTeam.player_id'))
    teams = db.relationship('FPLTeam', secondary=association_table, back_populates='players')
    user = db.relationship('User', back_populates='players')

