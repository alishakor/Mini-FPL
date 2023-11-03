#!/usr/bin/env python3
"""FPL Teams created by users"""
from models.basemodel import BaseModel, db

players_association_table = db.Table(
    'player_association',
    db.Column('team_id', db.String(128), db.ForeignKey('teams.id')),
    db.Column('player_id', db.String(128), db.ForeignKey('players.id'))
)

starting_player_association_table = db.Table(
    'starting_player_association',
    db.Column('team_id', db.String(128), db.ForeignKey('teams.id')),
    db.Column('player_id', db.String(128), db.ForeignKey('players.id')),
    db.Column("position", db.String(60))
)

bench_player_association_table = db.Table(
    'bench_player_association',
    db.Column('team_id', db.String(128), db.ForeignKey('teams.id')),
    db.Column('player_id', db.String(128), db.ForeignKey('players.id'))
)


class FPLTeam(BaseModel):
    __tablename__ = "teams"
    name = db.Column(db.String(128), unique=True, nullable=False)
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'), nullable=False, unique=True)
    points = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Numeric(precision=3, scale=1), nullable=False)
    players = db.relationship('Player', secondary=players_association_table)
    starting_players = db.relationship('Player', secondary=starting_player_association_table)
    bench_players = db.relationship('Player', secondary=bench_player_association_table)
    user = db.relationship('User', back_populates='team')
