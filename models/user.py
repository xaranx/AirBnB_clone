#!/usr/bin/python3
""" defines the User class"""
# import uuid
from models.base_model import BaseModel
# from datetime import datetime, date, time

class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#     def __init__(self, *args, **kwargs):
#         """
#         Instantiation of the class
#         """
#         self.id = str(uuid.uuid4())
#         self.created_at = datetime.now()
#         self.updated_at = datetime.now()

#         if len(kwargs) > 0:
#             super().__init__(*args, **kwargs)

#         from models.__init__ import storage
#         storage.new(self)
