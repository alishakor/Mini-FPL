#!/usr/bin/env python3
"""FPL Teams created by users"""
from models.basemodel import BaseModel, db


class FPLTeam(BaseModel):
    __tablename__ = "teams"
    name = db.Column(db.String(128), unique=True, nullable=False)
    team_id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Numeric(precision=3, scale=1), nullable=False)
    user = db.relationship('User', backref="teams")

