#!/usr/bin/python3
"""Module Test Case for FileStorage"""
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from datetime import datetime
from fileStorage.storage import FileStorage
from models.base_model import baseModel
from models.user import User
from models.country import Country
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """FileStorage Test Class"""
    @classmethod
    def setUpClass(cls):
        cls.p1 = Place('name', 'description', 'address', 'city', 'latitude', 'longitude', 'host', 'number_of_rooms', 'number_of_bathrooms', 'max_guests', 'price_per_night')
        cls.p1.city_id = "Richmond"
        cls.p1.state_id = "VA"
        cls.p1.number_rooms = 8
        cls.p1.description = "awesome"

    @classmethod
    def tearDownClass(cls):
        del cls.p1

    def tearDown(self):
        """TearDown for each method in TestFileStorage class"""
        FileStorage.delete_all(self)
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_fs_instance(self):
        """FileStorage class save checks, reload checks"""
        b1 = baseModel()
        FileStorage.save(self)
        self.assertEqual(os.path.exists('file.json'), False)

        FileStorage.delete_all(self)
        FileStorage.load(self)

    def test_errs(self):
        """Test most mal usage of FileStorage methods"""
        b1 = baseModel()
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__File_path

        with self.assertRaises(TypeError):
            FileStorage.new()
            FileStorage.new(self, b1)
            FileStorage.save(b1)
            FileStorage.load(b1)
            FileStorage.all(b1)


if __name__ == '__main__':
    unittest.main()
