#!/usr/bin/python3
"""
"""
base_model = __import__('base_model').base_model

class Review(base_model):
    """
    """
    def __init__(self, user, place, text, rating):
        """
        """
        super.__init__()
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
