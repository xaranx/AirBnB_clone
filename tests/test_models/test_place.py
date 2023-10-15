#!/usr/bin/python3
"""
Testing BaseModel class
"""
import models
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime, date, time
import unittest


class TestPlace(unittest.TestCase):
    """
    Tests Place class
    """
    def test_Place_basic(self):
        """
        Basic assertions to check the creation of an obj and its attrs
        """
        obj = Place()

        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(type(obj), Place)
        self.assertTrue(type(obj.id), str)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, '__class__'))

    def test_Place_unique_ids(self):
        """
        Testing the Uniqueness of ids
        """
        obj = Place()
        obj1 = Place()

        self.assertFalse(obj.id == obj1.id)

    def test_Place_attr_types(self):
        """
        Testing the types of a class attributes
        """
        obj = Place()

        self.assertTrue(obj.city_id == "")
        self.assertTrue(obj.user_id == "")
        self.assertTrue(obj.description == "")
        self.assertTrue(obj.number_rooms == 0)
        self.assertTrue(obj.number_bathrooms == 0)
        self.assertTrue(obj.max_guest == 0)
        self.assertTrue(obj.price_by_night == 0)
        self.assertTrue(obj.latitude == 0.0)
        self.assertTrue(obj.longitude == 0.0)
        self.assertTrue(obj.amenity_ids == [])
        self.assertTrue(type(obj.id), str)
        self.assertTrue(type(obj.__class__), str)
        self.assertTrue(type(obj.updated_at), datetime)
        self.assertTrue(type(obj.created_at), datetime)

    def test_user_str_method(self):
        """
        Testing Place.__str__ method
        """
        obj = Place()
        expected_str = "[{}] ({}) {}"\
            .format(obj.__class__.__name__, obj.id, obj.__dict__)

        self.assertTrue(obj.__str__() == expected_str)

    def test_Place_save_method(self):
        """
        Testing Place.save() method
        """
        obj = Place()

        self.assertTrue(obj.created_at == obj.updated_at)
        obj.save()
        self.assertFalse(obj.created_at == obj.updated_at)

    def test_Place_to_dict_method(self):
        """
        Testing Place.to_dict() method
        """
        obj = Place()

        self.assertFalse(obj.__dict__ == obj.to_dict())
        self.assertTrue(type(obj.to_dict()), dict)
        self.assertTrue(type(obj.to_dict()['created_at']), datetime)
        self.assertTrue(type(obj.to_dict()['updated_at']), datetime)
        self.assertTrue(hasattr(obj.to_dict(), '__class__'))
        self.assertTrue(obj.to_dict()['__class__'] == 'Place')
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj, Place)


if __name__ == "__main__":
    unittest.main()
