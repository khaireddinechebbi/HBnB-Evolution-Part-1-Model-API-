#!/usr/bin/python3
"""
Module for baseModel class
"""
import uuid
from datetime import datetime


class baseModel:
    """
    Class that defines common attributes and methods for other classes

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Timestamp when the instance was created.
        updated_at (datetime): Timestamp when the instance was last updated.
    """

    def __init__(self):
        """
        Initialize a new instance of baseModel
        Generates a unique ID and sets the creation and update timestamps.
        """
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __repr__(self):
        """
        Return a string representation of the instance.
        """
        return self.__str__()

    def save(self):
        """
        Update the updated_at timestamp
        This method should be called whenever the instance is modified.
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Convert instance attributes to a dictionary format
        Returns:
            dict: Dictionary containing the instance attributes.
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
