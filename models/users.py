#!/usr/bin/env python3
"""
fpl users module
"""
<<<<<<< HEAD
from models.basemodel import BaseModel, db
=======
from basemodel import BaseModel, db
from flask_login import UserMixin
>>>>>>> 6c0088702e1eeb7e6b67b6457850265c7027e6b1


class User(UserMixin, BaseModel):
    """
    The User class contains all the user's info
    """
    __tablename__ = 'users'
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)
    verification_code = db.Column(db.String(128), nullable=False, unique=True)
    verified = db.Column(db.Integer, default=0)
