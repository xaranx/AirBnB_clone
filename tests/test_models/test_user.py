#!/usr/bin/python3
"""
Testing BaseModel class
"""
import models
from models.base_model import BaseModel
from models.user import User
from datetime import datetime, date, time
import unittest


class TestUser(unittest.TestCase):
    """
    Tests User class
    """
    def test_user_basic(self):
        """
        Basic assertions to check the creation of an obj and its attrs
        """
        obj = User()

        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(type(obj), User)
        self.assertTrue(type(obj.id), str)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, '__class__'))

    def test_user_unique_ids(self):
        """
        Testing the Uniqueness of ids
        """
        obj = User()
        obj1 = User()

        self.assertFalse(obj.id == obj1.id)

    def test_user_attr_types(self):
        """
        Testing the types of a class attributes
        """
        obj = User()

        self.assertTrue(type(obj.email), str)
        self.assertTrue(type(obj.first_name), str)
        self.assertTrue(type(obj.password), str)
        self.assertTrue(type(obj.last_name), str)
        self.assertTrue(type(obj.id), str)
        self.assertTrue(type(obj.__class__), str)
        self.assertTrue(type(obj.updated_at), datetime)
        self.assertTrue(type(obj.created_at), datetime)

    def test_user_str_method(self):
        """
        Testing User.__str__ method
        """
        user = User()
        expected_str = "[{}] ({}) {}"\
            .format(user.__class__.__name__, user.id, user.__dict__)

        self.assertTrue(user.__str__() == expected_str)

    def test_user_save_method(self):
        """
        Testing user.save() method
        """
        usr_obj = User()

        self.assertTrue(usr_obj.created_at == usr_obj.updated_at)
        usr_obj.save()
        self.assertFalse(usr_obj.created_at == usr_obj.updated_at)

    def test_user_to_dict_method(self):
        """
        Testing user.to_dict() method
        """
        obj = User()

        self.assertFalse(obj.__dict__ == obj.to_dict())
        self.assertTrue(type(obj.to_dict()), dict)
        self.assertTrue(type(obj.to_dict()['created_at']), datetime)
        self.assertTrue(type(obj.to_dict()['updated_at']), datetime)
        self.assertTrue(hasattr(obj, 'email'))
        self.assertTrue(hasattr(obj, 'password'))
        self.assertTrue(hasattr(obj, 'first_name'))
        self.assertTrue(hasattr(obj, 'last_name'))
        self.assertTrue(hasattr(obj, '__class__'))
        self.assertTrue(obj.to_dict()['__class__'] == 'User')
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj, User)


if __name__ == "__main__":
    unittest.main()
