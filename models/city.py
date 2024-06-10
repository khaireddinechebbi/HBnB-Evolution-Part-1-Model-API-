#!/usr/bin/python3
"""
"""
from models.base_model import base_model

class City(base_model):
    """
    """
    def __init__(self, name, country):
        """
        """
        super().__init__()
        self.name = name
        self.country = country
