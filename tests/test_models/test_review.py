#!/usr/bin/python3
"""
Testing BaseModel class
"""
import models
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime, date, time
import unittest


class TestReview(unittest.TestCase):
    """
    Tests Review class
    """
    def test_Review_basic(self):
        """
        Basic assertions to check the creation of an obj and its attrs
        """
        obj = Review()

        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(type(obj), Review)
        self.assertTrue(type(obj.id), str)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, '__class__'))

    def test_Review_unique_ids(self):
        """
        Testing the Uniqueness of ids
        """
        obj = Review()
        obj1 = Review()

        self.assertFalse(obj.id == obj1.id)

    def test_Review_attr_types(self):
        """
        Testing the types of a class attributes
        """
        obj = Review()

        self.assertTrue(type(obj.id), str)
        self.assertTrue(type(obj.__class__), str)
        self.assertTrue(type(obj.updated_at), datetime)
        self.assertTrue(type(obj.created_at), datetime)

    def test_user_str_method(self):
        """
        Testing Review.__str__ method
        """
        obj = Review()
        expected_str = "[{}] ({}) {}"\
            .format(obj.__class__.__name__, obj.id, obj.__dict__)

        self.assertTrue(obj.__str__() == expected_str)

    def test_Review_save_method(self):
        """
        Testing Review.save() method
        """
        obj = Review()

        self.assertTrue(obj.created_at == obj.updated_at)
        obj.save()
        self.assertFalse(obj.created_at == obj.updated_at)

    def test_Review_to_dict_method(self):
        """
        Testing Review.to_dict() method
        """
        obj = Review()

        self.assertFalse(obj.__dict__ == obj.to_dict())
        self.assertTrue(type(obj.to_dict()), dict)
        self.assertTrue(type(obj.to_dict()['created_at']), datetime)
        self.assertTrue(type(obj.to_dict()['updated_at']), datetime)
        self.assertTrue(hasattr(obj.to_dict(), '__class__'))
        self.assertTrue(obj.to_dict()['__class__'] == 'Review')
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj, Review)


if __name__ == "__main__":
    unittest.main()
