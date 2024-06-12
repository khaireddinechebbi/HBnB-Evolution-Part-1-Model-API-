#!/usr/bin/python3
"""
"""
from models.base_model import baseModel

class City(baseModel):
    """
    """
    def __init__(self, name, country):
        """
        """
        super().__init__()
        self.name = name
        self.country = country
