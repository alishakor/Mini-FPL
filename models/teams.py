#!/usr/bin/env python3
"""FPL Teams created by users"""
from models.basemodel import BaseModel, db
from models.players import association_table

class FPLTeam(BaseModel):
    __tablename__ = "teams"
    name = db.Column(db.String(128), unique=True, nullable=False)
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'), nullable=False, unique=True)
    points = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Numeric(precision=3, scale=1), nullable=False)
    # Define the many-to-many relationship with Player
    players = db.relationship('Player', secondary=association_table, back_populates='teams')
    # Define the many-to-one relationship with User
    user = db.relationship('User', back_populates='teams', overlaps="user_teams")
