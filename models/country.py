#!/usr/bin/python3
"""
Country module containing the Country class
"""


class Country:
    """
    Country class representing a country and its cities

    Attributes:
        name (str): Name of the country.
        cities (list): List of cities in the country.
    """

    def __init__(self, name):
        """
        Initialize a new Country instance

        Args:
            name (str): The name of the country.
        """
        self.name = name
        self.cities = []

    def add_city(self, city):
        """
        Add a city to the country's list of cities

        Args:
            city (City): The city to be added.
        """
        self.cities.append(city)
