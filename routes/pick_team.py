#!/usr/bin/env python3
"""
team selection from squad
"""
import random
from flask import render_template
from flask_login import login_required
from models.teams import FPLTeam
from models.players import Player
from models.basemodel import app
from routes import pick_bp
import requests


api_url = "https://fantasy.premierleague.com/api/bootstrap-static/"


@pick_bp.route('/my_team',  methods=['GET', 'POST'], strict_slashes=False)
# @login_required
def index():
    """Select your fpl team"""
    fplteam = FPLTeam.query.all()
    return render_template('pick-team.html', fplteam=fplteam)
