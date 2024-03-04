#!/usr/bin/python3
"""Test State"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests"""

    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_state_to_dict(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()
