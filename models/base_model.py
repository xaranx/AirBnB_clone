#!/usr/bin/python3
"""
BaseModel Module
"""
import uuid
from datetime import datetime, date, time
from models.__init__ import storage
from models.engine.file_storage import FileStorage


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    now = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        Instantiation of the class
        """
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.fromisoformat(v))
                setattr(self, k, v)
        self.id = str(uuid.uuid4())
        self.created_at = BaseModel.now
        if __class__.__name__ + '.' + str(self.id) not in FileStorage.objects.keys():
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        cr, up = 'created_at', 'updated_at'
        dic = {k: (v.isoformat() if k == cr or k == up else v)
               for k, v in self.__dict__.items()
               }
        dic['__class__'] = __class__.__name__
        return dic
