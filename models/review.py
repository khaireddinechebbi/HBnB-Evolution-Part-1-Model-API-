#!/usr/bin/python3
"""
Review module containing the Review class
"""

from models.base_model import baseModel


class Review(baseModel):
    """
    Review class representing a review for a place

    Attributes:
        user (User): The user who wrote the review.
        place (Place): The place being reviewed.
        text (str): The text content of the review.
        rating (int): The rating given in the review.
    """

    def __init__(self, user, place, text, rating):
        """
        Initialize a new Review instance

        Args:
            user (User): The user who wrote the review.
            place (Place): The place being reviewed.
            text (str): The text content of the review.
            rating (int): The rating given in the review.
        """
        super().__init__()
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
