#!/usr/bin/env python3

from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
players_bp = Blueprint('players', __name__, url_prefix='/')
fixtures_bp = Blueprint('fixtures', __name__, url_prefix='/')
create_bp = Blueprint('team_create', __name__, url_prefix='/')
pick_bp = Blueprint('my_team', __name__, url_prefix='/')


from routes.auth import *
from routes.players import *
from routes.status import *
from routes.fixtures import *
from routes.create_team import *
from routes.pick_team import *
