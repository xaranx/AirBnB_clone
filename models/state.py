#!/usr/bin/python3
"""Defines the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    name (str): the name of the state
    """
    name = ""

#     def __init__(self, *args, **kwargs):
#         """
#         Instantiation of the class
#         """
#         super().__init__(*args, **kwargs)
#         self.save()
