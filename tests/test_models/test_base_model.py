#!/usr/bin/python3
"""Test BaseModel"""


import unittest  # Import the unittest module.
from datetime import datetime  # Import the datetime module.
from models.base_model import BaseModel # Import the class BaseModel.


class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        """Test BaseModel attributes initialization"""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test __str__ method"""
        model = BaseModel()
        self.assertIsInstance(str(model), str)

    def test_save_method(self):
        """Test save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.fromisoformat(model_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(model_dict['updated_at']), datetime)

    def test_create_kwargs(self):
        """Test kwargs"""
        model = BaseModel()
        model_dict = model.to_dict()
        kwargs = BaseModel(model_dict)
        self.assertIsInstance(kwargs, BaseModel)

if __name__ == '__main__':
    unittest.main()
