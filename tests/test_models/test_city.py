#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_state_id_attribute(self):
        """Test state_id attribute"""
        new_city = self.value()
        self.assertEqual(type(new_city.state_id), str)

    def test_name_attribute(self):
        """Test name attribute"""
        new_city = self.value()
        self.assertEqual(type(new_city.name), str)

    def test_places_relationship(self):
        """Test places relationship"""
        new_city = self.value()
        self.assertTrue(hasattr(new_city, "places"))


if __name__ == '__main__':
    unittest.main()
