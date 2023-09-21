#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
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
