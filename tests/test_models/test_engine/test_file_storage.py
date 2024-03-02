#!/usr/bin/python3
"""Test FileStorage"""


import unittest  # Import the unittest module.
from models.engine.file_storage import FileStorage  # Import the class FS.
from models.base_model import BaseModel  # Import the class BaseModel.


class TestFileStorage(unittest.TestCase):
    """Tests"""

    def test_all(self):
        """Test all() method"""
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test new() method"""
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertFalse(key in storage.all())

    def test_save(self):
        """Test save() method"""
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertTrue(data)

    def test_reload(self):
        """Test reload() method"""
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        storage.save()
        storage.reload()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertTrue(key in storage.all())

if __name__ == '__main__':
    unittest.main()
