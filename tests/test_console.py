#!/usr/bin/python3
"""
Testing the console
"""
# import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import unittest


class TestHBNBCommand(unittest.TestCase):
    """
    Testing the console
    """
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("help show")
