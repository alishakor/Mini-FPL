# #!/usr/bin/env python3
# """FPL fixtures"""
# from models.basemodel import BaseModel, db
#
# class Fixtures(BaseModel):
#     __tablename__ = "fixtures"
#     home_team_id = db.Column(db.String(128), db.ForeignKey("teams.id"))
#     away_team_id = db.Column(db.String(128), db.ForeignKey("teams.id"))
#     kickoff_time = db.Column(db.DateTime, nullable=False)
#
#     # Define the relationship for home and away fixtures
#     home_fixtures = db.relationship('Fixtures', foreign_keys=['fixtures.home_team_id'], backref='home_team_fixtures',
#                                     lazy='select')
#     away_fixtures = db.relationship('Fixtures', foreign_keys=['fixtures.away_team_id'], backref='away_team_fixtures',
#                                     lazy='select')
