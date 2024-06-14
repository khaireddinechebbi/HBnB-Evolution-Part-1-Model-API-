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
        a_dict = {}
        for key in file_storage.__obj:
            a_dict[key] = file_storage.__obj[key].to_dict()
        
        with open(file_storage.__filename, 'w') as file:
            json.dump(a_dict, file)

    def load(self):
        """
        """
        try:
            with open(file_storage.__filename, 'r') as f:
                a_dict = json.load(f)
            for key, value in a_dict.items():
                file_storage.__obj[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
    
    def new(self, object):
        """
        """
        key = object.__class__.__name__ + "." + object.id
        file_storage.__obj[key] = object

    def delete_obj(self):
        file_storage.__obj.clear()
