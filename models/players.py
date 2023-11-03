#!/usr/bin/env python3
"""players db module"""
from models.basemodel import BaseModel, db


class Player(BaseModel):
    __tablename__ = "players"
    name = db.Column(db.String(128), unique=True, nullable=False)
    club = db.Column(db.String(60), nullable=False)
    position = db.Column(db.String(60), nullable=False)
    point = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(256))
    selected_by_percentage = db.Column(db.String(60))
    points_per_game = db.Column(db.String(60))


