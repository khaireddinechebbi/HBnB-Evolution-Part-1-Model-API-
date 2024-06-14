#!/usr/bin/python3
"""Module Test Case for FileStorage"""
import unittest, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from datetime import datetime


import pep8
import models
from fileStorage.storage import *
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
        file_storage.delete_obj(self)
        if os.path.exists('file.json'):
            os.remove('file.json')



    def test_fs_instance(self):
        """FileStorage class save checks, reload checks"""
        b1 = baseModel()
        file_storage.save(self)
        self.assertEqual(os.path.exists('file.json'), False)

        file_storage.delete_obj(self)
        file_storage.load(self)

    def test_errs(self):
        """Test most mal usage of FileStorage methods"""
        b1 = baseModel()
        with self.assertRaises(AttributeError):
            file_storage.__objects
            file_storage.__File_path

        with self.assertRaises(TypeError):
            file_storage.new()
            file_storage.new(self, b1)
            file_storage.save(b1)
            file_storage.load(b1)
            file_storage.all(b1)

if __name__ == '__main__':
    unittest.main()
