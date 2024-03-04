#!/usr/bin/python3
"""Test User"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests"""

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")

    def test_user_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()
