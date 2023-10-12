#!/usr/bin/env python3
"""
fpl users module
"""
from basemodel import BaseModel, db


class User(BaseModel):
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
