#!/usr/bin/python3
"""Test City"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests"""

    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")

    def test_city_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')


if __name__ == '__main__':
    unittest.main()
