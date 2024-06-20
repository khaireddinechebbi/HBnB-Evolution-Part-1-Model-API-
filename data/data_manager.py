#!/usr/bin/python3
"""
Data manager for the application.
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user import User
from models.review import Review
from models.place import Place
from models.country import Country
from models.city import City
from models.amenity import Amenity
from persistence.user_repository import UserRepository
from persistence.review_repository import ReviewRepository
from persistence.place_repository import PlaceRepository
from persistence.country_repository import CountryRepository
from persistence.city_repository import CityRepository
from persistence.amenity_repository import AmenityRepository


class DataManager:
    """
    Class to manage CRUD operations for various entities.
    """

    def __init__(self):
        self.place_repository = PlaceRepository()
        self.user_repository = UserRepository()
        self.review_repository = ReviewRepository()
        self.amenity_repository = AmenityRepository()
        self.country_repository = CountryRepository()
        self.city_repository = CityRepository()

    # Methods for Place
    def save_place(self, place_data):
        """
        Save a new place.

        Args:
            place_data (dict): Data for the new place.

        Returns:
            str: The ID of the saved place.
        """
        place = Place(**place_data)
        self.place_repository.save(place)
        return place.place_id

    def get_place(self, place_id):
        """
        Get a place by ID.

        Args:
            place_id (str): The ID of the place to retrieve.

        Returns:
            Place: The place object.
        """
        return self.place_repository.get(place_id)

    def update_place(self, place_id, new_data):
        """
        Update a place by ID.

        Args:
            place_id (str): The ID of the place to update.
            new_data (dict): The new data for the place.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.place_repository.update(place_id, new_data)

    def delete_place(self, place_id):
        """
        Delete a place by ID.

        Args:
            place_id (str): The ID of the place to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        return self.place_repository.delete(place_id)

    def get_all_places(self):
        """
        Get all places.

        Returns:
            list: A list of all place objects.
        """
        return self.place_repository.get_all()

    # Methods for User
    def save_user(self, user_data):
        """
        Save a new user.

        Args:
            user_data (dict): Data for the new user.

        Returns:
            str: The ID of the saved user.
        """
        user = User(**user_data)
        self.user_repository.save(user)
        return user.user_id

    def get_user(self, user_id):
        """
        Get a user by ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            User: The user object.
        """
        return self.user_repository.get(user_id)

    def update_user(self, user_id, new_data):
        """
        Update a user by ID.

        Args:
            user_id (str): The ID of the user to update.
            new_data (dict): The new data for the user.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.user_repository.update(user_id, new_data)

    def delete_user(self, user_id):
        """
        Delete a user by ID.

        Args:
            user_id (str): The ID of the user to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        return self.user_repository.delete(user_id)

    def get_all_users(self):
        """
        Get all users.

        Returns:
            list: A list of all user objects.
        """
        return self.user_repository.get_all()

    # Methods for Review
    def save_review(self, review_data):
        """
        Save a new review.

        Args:
            review_data (dict): Data for the new review.

        Returns:
            str: The ID of the saved review.
        """
        review = Review(**review_data)
        self.review_repository.save(review)
        return review.review_id

    def get_review(self, review_id):
        """
        Get a review by ID.

        Args:
            review_id (str): The ID of the review to retrieve.

        Returns:
            Review: The review object.
        """
        return self.review_repository.get(review_id)

    def update_review(self, review_id, new_data):
        """
        Update a review by ID.

        Args:
            review_id (str): The ID of the review to update.
            new_data (dict): The new data for the review.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.review_repository.update(review_id, new_data)

    def delete_review(self, review_id):
        """
        Delete a review by ID.

        Args:
            review_id (str): The ID of the review to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        return self.review_repository.delete(review_id)

    def get_all_reviews(self):
        """
        Get all reviews.

        Returns:
            list: A list of all review objects.
        """
        return self.review_repository.get_all()

    # Methods for Amenity
    def save_amenity(self, amenity_data):
        """
        Save a new amenity.

        Args:
            amenity_data (dict): Data for the new amenity.

        Returns:
            str: The ID of the saved amenity.
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repository.save(amenity)
        return amenity.amenity_id

    def get_amenity(self, amenity_id):
        """
        Get an amenity by ID.

        Args:
            amenity_id (str): The ID of the amenity to retrieve.

        Returns:
            Amenity: The amenity object.
        """
        return self.amenity_repository.get(amenity_id)

    def update_amenity(self, amenity_id, new_data):
        """
        Update an amenity by ID.

        Args:
            amenity_id (str): The ID of the amenity to update.
            new_data (dict): The new data for the amenity.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.amenity_repository.update(amenity_id, new_data)

    def delete_amenity(self, amenity_id):
        """
        Delete an amenity by ID.

        Args:
            amenity_id (str): The ID of the amenity to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        return self.amenity_repository.delete(amenity_id)

    def get_all_amenities(self):
        """
        Get all amenities.

        Returns:
            list: A list of all amenity objects.
        """
        return self.amenity_repository.get_all()

    # Methods for Country
    def save_country(self, country_data):
        """
        Save a new country.

        Args:
            country_data (dict): Data for the new country.

        Returns:
            str: The ID of the saved country.
        """
        country = Country(**country_data)
        self.country_repository.save(country)
        return country.country_id

    def get_country(self, country_id):
        """
        Get a country by ID.

        Args:
            country_id (str): The ID of the country to retrieve.

        Returns:
            Country: The country object.
        """
        return self.country_repository.get(country_id)

    def update_country(self, country_id, new_data):
        """
        Update a country by ID.

        Args:
            country_id (str): The ID of the country to update.
            new_data (dict): The new data for the country.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.country_repository.update(country_id, new_data)

    def delete_country(self, country_id):
        """
        Delete a country by ID.

        Args:
            country_id (str): The ID of the country to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        return self.country_repository.delete(country_id)

    def get_all_countries(self):
        """
        Get all countries.

        Returns:
            list: A list of all country objects.
        """
        return self.country_repository.get_all()

    # Methods for City
    def save_city(self, city_data):
        """
        Save a new city.

        Args:
            city_data (dict): Data for the new city.

        Returns:
            str: The ID of the saved city.
        """
        city = City(**city_data)
        self.city_repository.save(city)
        return city.city_id

    def get_city(self, city_id):
        """
        Get a city by ID.

        Args:
            city_id (str): The ID of the city to retrieve.

        Returns:
            City: The city object.
        """
        return self.city_repository.get(city_id)

    def update_city(self, city_id, new_data):
        """
        Update a city by ID.

        Args:
            city_id (str): The ID of the city to update.
            new_data (dict): The new data for the city.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        return self.city_repository.update(city_id, new_data)

    def delete_city(self, city_id):
        """
        Delete a city by ID.

        Args:
            city_id (str): The ID of the city to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        return self.city_repository.delete(city_id)

    def get_all_cities(self):
        """
        Get all cities.

        Returns:
            list: A list of all city objects.
        """
        return self.city_repository.get_all()
