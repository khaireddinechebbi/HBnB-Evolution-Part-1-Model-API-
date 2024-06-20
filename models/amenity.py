#!/usr/bin/python3
"""
Module for Amenity class
"""
from models.base_model import baseModel


class Amenity(baseModel):
    """
    Amenity class inheriting from baseModel

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, name):
        """
        Initialize an Amenity instance

        Args:
            name (str): The name of the amenity.
        """
        super().__init__()
        self.name = name
