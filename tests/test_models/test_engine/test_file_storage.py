#!/usr/bin/python3
"""
Testing FileStorage class
"""
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
# from models.__init__ import storage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Testing FileStorage class
    """
    def test_basic(self):
        """
        Testing basic tests on FileStorage class
        """
        obj = FileStorage()
        data = obj.all()

        self.assertIsInstance(obj, FileStorage)
        self.assertTrue(type(data), dict)
        self.assertTrue(len(data) > 0)
        self.assertTrue(hasattr(obj, f'_{obj.__class__.__name__}__objects'))
        self.assertTrue(hasattr(obj, f'_{obj.__class__.__name__}__file_path'))

        obj.save()
        self.assertTrue(os.path.exists('file.json'))


if __name__ == "__main__":
    unittest.main()
