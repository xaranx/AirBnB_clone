#!/usr/bin/python3
"""defines the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    name (str): the name of the Amenity
    """
    name = ""

    # def __init__(self, *args, **kwargs):
    #     """
    #     Instantiation of the class
    #     """
    #     super().__init__(*args, **kwargs)
    #     self.save()
