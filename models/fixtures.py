#!/usr/bin/env python3
"""FPL fixtures"""
from models.basemodel import BaseModel, db


class Fixtures(BaseModel):
    __tablename__ = "fixtures"
    fixture_id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.String(128), db.ForeignKey("teams.id"))
    away_team_id = db.Column(db.String(128), db.ForeignKey("teams.id"))
    kickoff_time = db.Column(db.DateTime, nullable=False)
    home_team = db.relationship('Team', foreign_keys=[home_team_id], backref='home_fixtures')
    away_team = db.relationship('Team', foreign_keys=[away_team_id], backref='away_fixtures')

