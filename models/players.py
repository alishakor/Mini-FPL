#!/usr/bin/env python3
"""
fpl players module
"""
from models.base_model import BaseModel


class Player(BaseModel):
    """
    The Team class that inherits from base class
    """
    __tablename__ = 'players'
    team_id = db.Column(db.String(128), foreign_key=True,
                        unique=True, nullable=False)
    player_name = db.Column(db.String(128), unique=True, nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=100)
