#!/user/bin/python3
"""
"""
import json

class file_storage:
    """
    """

    __filename = "FileStorage.json"
    __obj = {}

    def print_all(self):
        """
        """
        return file_storage.__obj

    def save(self):
        """
        """
        for k, v in file_storage.__obj.items():
            with open(file_storage.__filename, 'w') as f:
                json.dump({k: v.to_dict()}, f)

    def load(self):
        """
        """
        try:
            with open(file_storage.__filename, 'r') as f:
                file_storage.__obj = json.load(f)
        except FileNotFoundError:
            pass
    
    def new(self, object):
        key = object.__class__.__name__ + "." + object.id
        file_storage.__obj[key] = object
