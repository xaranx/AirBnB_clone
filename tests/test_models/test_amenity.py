#!/usr/bin/python3
"""
Testing BaseModel class
"""
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime, date, time
import unittest


class TestAmenity(unittest.TestCase):
    """
    Tests Amenity class
    """
    def test_Amenity_basic(self):
        """
        Basic assertions to check the creation of an obj and its attrs
        """
        obj = Amenity()

        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(type(obj), Amenity)
        self.assertTrue(type(obj.id), str)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, '__class__'))

    def test_Amenity_unique_ids(self):
        """
        Testing the Uniqueness of ids
        """
        obj = Amenity()
        obj1 = Amenity()

        self.assertFalse(obj.id == obj1.id)

    def test_Amenity_attr_types(self):
        """
        Testing the types of a class attributes
        """
        obj = Amenity()

        self.assertTrue(type(obj.id), str)
        self.assertTrue(type(obj.__class__), str)
        self.assertTrue(type(obj.updated_at), datetime)
        self.assertTrue(type(obj.created_at), datetime)

    def test_user_str_method(self):
        """
        Testing Amenity.__str__ method
        """
        obj = Amenity()
        expected_str = "[{}] ({}) {}"\
            .format(obj.__class__.__name__, obj.id, obj.__dict__)

        self.assertTrue(obj.__str__() == expected_str)

    def test_Amenity_save_method(self):
        """
        Testing Amenity.save() method
        """
        obj = Amenity()

        self.assertTrue(obj.created_at == obj.updated_at)
        obj.save()
        self.assertFalse(obj.created_at == obj.updated_at)

    def test_Amenity_to_dict_method(self):
        """
        Testing Amenity.to_dict() method
        """
        obj = Amenity()

        self.assertFalse(obj.__dict__ == obj.to_dict())
        self.assertTrue(type(obj.to_dict()), dict)
        self.assertTrue(type(obj.to_dict()['created_at']), datetime)
        self.assertTrue(type(obj.to_dict()['updated_at']), datetime)
        self.assertTrue(hasattr(obj.to_dict(), '__class__'))
        self.assertTrue(obj.to_dict()['__class__'] == 'Amenity')
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj, Amenity)


if __name__ == "__main__":
    unittest.main()
