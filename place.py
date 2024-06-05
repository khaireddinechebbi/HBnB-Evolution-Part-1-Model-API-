#!/user/bin/python3
"""
"""
base_model = __import__('base_model').base_model
user = __import__('user').user

class place(base_model):
    """
    """
    def __init__(self, name, description, address, city, latitude, longitude, host, number_of_rooms, number_of_bathrooms, max_guests, price_per_night):
        """
        """
        super.__init__()
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
        """
        if amenity not in self.amenities:
            self.amenities.append(amenity)
    
    def add_review(self, review):
        """
        """
        self.reviews.append(review)