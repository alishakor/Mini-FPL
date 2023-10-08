#!/usr/bin/env python3
"""
Handles database configuration and loads all environment variables
"""

from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

user = getenv("FPL_USER")
database = getenv("FPL_DB")
password = getenv("FPL_PWD")
host = getenv("FPL_HOST")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{password}@{host}/{database}'
db = SQLAlchemy(app)
