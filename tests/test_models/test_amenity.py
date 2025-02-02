#!/usr/bin/python3
"""Unit tests for Amenity class"""
import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """Test Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize test class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name_attribute(self):
        """Test name attribute"""
        new_amenity = self.value()
        self.assertEqual(type(new_amenity.name), str)

    def test_place_amenities_relationship(self):
        """Test place_amenities relationship"""
        new_amenity = self.value()
        self.assertTrue(hasattr(new_amenity, "place_amenities"))


if __name__ == '__main__':
    unittest.main()
