#!/usr/bin/env python3
"""
Handles database configuration and loads all environment variables
"""

import os
from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

user = getenv("FPL_USER")
database = getenv("FPL_DB")
password = getenv("FPL_PWD")
host = getenv("FPL_HOST")

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{password}@{host}/{database}'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)