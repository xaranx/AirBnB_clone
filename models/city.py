#!/usr/bin/python3
""" Defines City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    state_id (str): the state id
    name (str):city name
    """
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """
        Instantiation of the class
        """
        super().__init__(*args, **kwargs)
        self.save()
