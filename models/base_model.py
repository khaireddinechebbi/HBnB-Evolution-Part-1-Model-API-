#!/usr/bin/python3
"""
"""
import uuid
from datetime import datetime

class baseModel:
    """
    """
    def __init__(self):
        """
        """
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

    def __repr__(self):
        return self.__str__()
    
    def save(self):
        """
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
