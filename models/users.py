#!/usr/bin/env python3
"""
fpl users module
"""
from models.basemodel import BaseModel, db
from flask_login import UserMixin
import bcrypt
class User(BaseModel, db.Model, UserMixin):
    """
    The User class contains all the user's info
    """
    __tablename__ = 'users'
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=True)
    verification_code = db.Column(db.String(128), nullable=True, unique=True)
    verified = db.Column(db.Integer, default=0)
    players = db.relationship("Player", back_populates="user")
    teams = db.relationship("FPLTeam", backref="user_teams", uselist=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def hash_password(password):
        pwd_byte = bytes(password, encoding='utf-8')
        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(pwd_byte, salt)
        return hashed_pwd

    @staticmethod
    def check_password_hash(password_to_check, password_hash):
        pwd_byte = bytes(password_to_check, encoding='utf-8')
        return bcrypt.checkpw(pwd_byte, password_hash)