#!/usr/bin/env python3

"""
BaseModel class that other class inherits from
"""


from uuid import uuid4
from datetime import datetime
from config import app, db
from typing import Dict


class BaseModel(db.Model):
    """
    BaseModel Class
    Args:
        id: Random id generated using uuid4 for each table id column
        created_at: Represents the time each class was created
        updated_at: Represents the time each class was updated
    """
    __abstract__ = True
    id = db.Column(db.String(128), primary_key=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initialization method
        """
        super().__init__(*args, **kwargs)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Saves the current session into the database
        :return:
            The details of the saved session
        """
        self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()

    def delete(self) -> Dict:
        """
        Deletes the current session from the database
        :return:
            An empty dict
        """
        db.session.delete(self)
        db.session.commit()

    def close(self):
        """
        Closes the current database Connection
        :return:
            Nothing
        """
        db.session.remove()

    def to_dict(self) -> Dict:
        """
        Returns a dictionary representation of the object.
        """
        attributes = {}
        for column in self.__table__.columns:
            attribute_name = column.name
            attribute_value = getattr(self, attribute_name)
            attributes[attribute_name] = attribute_value
        return attributes

    @classmethod
    def all(cls):
        """
        Retrieves all the objects of the current session
        :return:
            The retrieved object details
        """
        return cls.query.all()

    @classmethod
    def get(cls, obj_id: str) -> None:
        """
        Retrieve an object by its id.
        Returns the object if found, None otherwise.
        """
        if obj_id:
            return db.session.get(cls, obj_id)
        return None
