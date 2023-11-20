#!/usr/bin/env python3
"""Unittests for the models module"""

import unittest
from models.users import User
from models.teams import FPLTeam
from models.players import Player
from models.basemodel import db, app

# Create the objects of the classes
user = User()
player = Player()
team = FPLTeam()

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        with app.app_context():
            user = User(username="shkor", password="@testing", email="aliuoeowo@gmail.com", first_name="Aliu", last_name="Okeowo")
            db.session.add(user)
            db.session.commit()
            self.assertEqual(user.username, "shkor")

    def test_create_player(self):
        with app.app_context():
            player = Player(name="Mohammed Salah", image="https://resources.premierleague.com/premierleague/photos/players/110x140/p118748.png", points_per_game=5.5)
            db.session.add(player)
            db.session.commit()
            self.assertEqual(player.name, "Mohammed Salah")

    def test_create_team(self):
        with app.app_context():
            team = FPLTeam(name="Liverpool", user_id="1", points=0, budget=100.0)
            db.session.add(team)
            db.session.commit()
            self.assertEqual(team.name, "Liverpool")

    def test_get_players_info_from_team(self):
        with app.app_context():
            query = db.session.query(Player.name, Player.image, Player.points_per_game). \
                join(FPLTeam, Player.name == FPLTeam.name).all()
            self.assertEqual(query, [])

    def test_get_players_info_from_team(self):
        with app.app_context():
            query = db.session.query(Player.name, Player.image, Player.points_per_game). \
                join(FPLTeam, Player.name == FPLTeam.name).all()
            self.assertEqual(query, [])

    def test_get_players_info_from_team(self):
        with app.app_context():
            query = db.session.query(Player.name, Player.image, Player.points_per_game). \
                join(FPLTeam, Player.name == FPLTeam.name).all()
            self.assertEqual(query, [])


if __name__ == '__main__':
    unittest.main()
