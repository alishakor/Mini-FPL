#!/usr/bin/env python3
"""
fpl Team module
"""
from basemodel import BaseModel


class Team(BaseModel):
    """
    The Team class that inherits from base class
    """
    __tablename__ = 'teams'
    player_id = db.Column(db.String(128), foreign_key=True,
                          unique=True, nullable=False)
    team_name = db.Column(db.String(128), unique=True, nullable=False)
    budget = db.Column(db.integer, default=100)
