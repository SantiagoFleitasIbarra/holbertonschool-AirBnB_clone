#!/usr/bin/python3
"""Test Review"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests"""

    def test_review_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")

    def test_review_to_dict(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')


if __name__ == '__main__':
    unittest.main()
