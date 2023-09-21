#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from models.city import City


class test_City(unittest.TestCase):
    """Test cases for the City class"""

    def test_state_id_attribute(self):
        """Test state_id attribute"""
        new_city = City()
        self.assertEqual(type(new_city.state_id), str)

    def test_name_attribute(self):
        """Test name attribute"""
        new_city = City()
        self.assertEqual(type(new_city.name), str)

    def test_places_relationship(self):
        """Test places relationship"""
        new_city = City()
        self.assertTrue(hasattr(new_city, "places"))


if __name__ == '__main__':
    unittest.main()
