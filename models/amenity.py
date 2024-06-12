#!/usr/bin/python3
"""
"""
from models.base_model import baseModel

class Amenity(baseModel):
    """
    """
    def __init__(self, name):
        """
        """
        super().__init__()
        self.name = name
