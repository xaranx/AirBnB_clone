#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

#     def __init__(self, *args, **kwargs):
#         """
#         Instantiation of the class
#         """
#         super().__init__(*args, **kwargs)
#         self.save()
