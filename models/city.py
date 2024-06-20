#!/usr/bin/python3
"""
City module containing the City class
"""
from models.base_model import baseModel


class City(baseModel):
    """
    City class that inherits from baseModel

    Attributes:
        name (str): Name of the city.
        country (str): Country where the city is located.
    """

    def __init__(self, name, country):
        """
        Initialize a new City instance

        Args:
            name (str): The name of the city.
            country (str): The country where the city is located.
        """
        super().__init__()
        self.name = name
        self.country = country
