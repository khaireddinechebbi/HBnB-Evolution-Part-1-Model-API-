#!/usr/bin/python3
"""
Module for file storage system
"""

import json


class FileStorage:
    """
    FileStorage class for serializing and deserializing objects to\
          and from JSON files.

    Attributes:
        __filename (str): Name of the file to save the objects.
        __obj (dict): Dictionary to store objects in memory.
    """

    __filename = "FileStorage.json"
    __obj = {}

    def print_all(self):
        """
        Return all objects stored in memory.

        Returns:
            dict: Dictionary of all objects.
        """
        return FileStorage.__obj

    def save(self):
        """
        Serialize objects to a JSON file.
        """
        a_dict = {}
        for key in FileStorage.__obj:
            a_dict[key] = FileStorage.__obj[key].to_dict()

        with open(FileStorage.__filename, 'w') as file:
            json.dump(a_dict, file)

    def load(self):
        """
        Deserialize objects from a JSON file.
        """
        try:
            with open(FileStorage.__filename, 'r') as f:
                a_dict = json.load(f)
            for key, value in a_dict.items():
                FileStorage.__obj[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj (object): The object to add.
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__obj[key] = obj

    def delete_all(self):
        """
        Delete all objects from the storage.
        """
        FileStorage.__obj.clear()
