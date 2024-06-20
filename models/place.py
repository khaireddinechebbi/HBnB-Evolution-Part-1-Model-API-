#!/usr/bin/python3
"""
Place module containing the Place class
"""

from models.base_model import baseModel
from models.user import User


class Place(baseModel):
    """
    Place class representing a place for rent

    Attributes:
        name (str): Name of the place.
        description (str): Description of the place.
        address (str): Address of the place.
        city (str): City where the place is located.
        latitude (float): Latitude of the place's location.
        longitude (float): Longitude of the place's location.
        host (User): Host of the place.
        number_of_rooms (int): Number of rooms in the place.
        number_of_bathrooms (int): Number of bathrooms in the place.
        max_guests (int): Maximum number of guests the place can accommodate.
        price_per_night (float): Price per night for renting the place.
        amenities (list): List of amenities available at the place.
        reviews (list): List of reviews for the place.
    """

    def __init__(
            self,
            name,
            description,
            address,
            city,
            latitude,
            longitude,
            host,
            number_of_rooms,
            number_of_bathrooms,
            max_guests,
            price_per_night):
        """
        Initialize a new Place instance

        Args:
            name (str): Name of the place.
            description (str): Description of the place.
            address (str): Address of the place.
            city (str): City where the place is located.
            latitude (float): Latitude of the place's location.
            longitude (float): Longitude of the place's location.
            host (User): Host of the place.
            number_of_rooms (int): Number of rooms in the place.
            number_of_bathrooms (int): Number of bathrooms in the place.
            max_guests (int): Max. number of guests the place can accommodate.
            price_per_night (float): Price per night for renting the place.
        """
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        """
        Add an amenity to the place's list of amenities

        Args:
            amenity (str): The amenity to be added.
        """
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        """
        Add a review to the place's list of reviews

        Args:
            review (str): The review to be added.
        """
        self.reviews.append(review)
