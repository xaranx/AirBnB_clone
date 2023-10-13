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
    def __init__(self, *args, **kwargs):
        """
        The class constructor
        Arguments: *args, **kwargs
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue

                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v, time_format))

                else:
                    setattr(self, k, v)

        from models.__init__ import storage
        storage.new(self)

    def __str__(self):
        """
        Returns the instance representation
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        from models.__init__ import storage
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dic = self.__dict__.copy()

        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic['__class__'] = __class__.__name__

        return dic
