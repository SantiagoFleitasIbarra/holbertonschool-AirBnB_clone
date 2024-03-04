#!/usr/bin/python3
"""Test Place"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests"""

    def test_place_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.amenity_ids, [])

    def test_place_to_dict(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')


if __name__ == '__main__':
    unittest.main()
