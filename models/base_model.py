#!/usr/bin/python3
"""
BaseModel Module
"""
import uuid
from datetime import datetime, date, time


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    now = datetime.now()

    def __init__(self, id=str(uuid.uuid4()), created_at=now, updated_at=now):
        """
        Instantiation of the class
        """
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """
        Returns the instance representation
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dic = {k: v for k, v in self.__dict__.items()}
        dic['__class__'] = __class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
