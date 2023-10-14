#!/usr/bin/python3
"""
Testing BaseModel class
"""
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from datetime import datetime, date, time
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Tests BaseModel class
    """
    def test_basic(self):
        """
        Basic assertions to check the creation of an obj and its attrs
        """
        obj = BaseModel()

        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(type(obj.id), str)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, '__class__'))

    def test_unique_ids(self):
        """
        Testing the Uniqueness of ids
        """
        obj = BaseModel()
        obj1 = BaseModel()

        self.assertFalse(obj.id == obj1.id)

    def test_attr_types(self):
        """
        Testing the types of a class attributes
        """
        obj = BaseModel()

        self.assertTrue(type(obj.id), str)
        self.assertTrue(type(obj.__class__), str)
        self.assertTrue(type(obj.updated_at), datetime)
        self.assertTrue(type(obj.created_at), datetime)

    def test_class_str_method(self):
        """
        Testing __class__.__name__.__str__ method
        """
        base = BaseModel()
        expected_str = "[{}] ({}) {}"\
            .format(base.__class__.__name__, base.id, base.__dict__)

        self.assertTrue(base.__str__() == expected_str)

        user = User()
        expected_str = "[{}] ({}) {}"\
            .format(user.__class__.__name__, user.id, user.__dict__)

        self.assertTrue(user.__str__() == expected_str)

        city = City()
        expected_str = "[{}] ({}) {}"\
            .format(city.__class__.__name__, city.id, city.__dict__)

        self.assertTrue(city.__str__() == expected_str)

    def test_class_save_method(self):
        """
        Testing __class__.__name__.save() method
        """
        obj = BaseModel()
        usr_obj = User()

        self.assertTrue(obj.created_at == obj.updated_at)
        obj.save()
        self.assertFalse(obj.created_at == obj.updated_at)

        self.assertTrue(usr_obj.created_at == usr_obj.updated_at)
        usr_obj.save()
        self.assertFalse(usr_obj.created_at == usr_obj.updated_at)

    def test_class_to_dict_method(self):
        """
        Testing __class__.__name__.to_dict() method
        """
        obj = BaseModel()
        state = State()

        self.assertFalse(obj.__dict__ == obj.to_dict())
        self.assertTrue(type(obj.to_dict()), dict)
        self.assertTrue(type(obj.to_dict()['created_at']), datetime)
        self.assertTrue(type(obj.to_dict()['updated_at']), datetime)
        self.assertTrue(hasattr(obj.to_dict(), '__class__'))

        self.assertFalse(state.__dict__ == state.to_dict())
        self.assertTrue(type(state.to_dict()), dict)
        self.assertTrue(type(state.to_dict()['created_at']), datetime)
        self.assertTrue(type(state.to_dict()['updated_at']), datetime)
        self.assertTrue(hasattr(state.to_dict(), '__class__'))
        self.assertTrue(state.to_dict()['__class__'] == 'State')
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state, State)


if __name__ == "__main__":
    unittest.main()
