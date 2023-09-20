#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name_attribute(self):
        """Test name attribute"""
        new_state = self.value()
        self.assertEqual(type(new_state.name), str)

if __name__ == '__main__':
    unittest.main()
