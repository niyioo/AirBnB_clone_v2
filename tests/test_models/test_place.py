#!/usr/bin/python3
"""Unit tests for Place class"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_city_id_attribute(self):
        """Test city_id attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.city_id), str)

    def test_user_id_attribute(self):
        """Test user_id attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.user_id), str)

    def test_name_attribute(self):
        """Test name attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.name), str)

    def test_description_attribute(self):
        """Test description attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.description), str)

    def test_number_rooms_attribute(self):
        """Test number_rooms attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.number_rooms), int)

    def test_number_bathrooms_attribute(self):
        """Test number_bathrooms attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.number_bathrooms), int)

    def test_max_guest_attribute(self):
        """Test max_guest attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.max_guest), int)

    def test_price_by_night_attribute(self):
        """Test price_by_night attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.price_by_night), int)

    def test_latitude_attribute(self):
        """Test latitude attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.latitude), float)

    def test_longitude_attribute(self):
        """Test longitude attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.longitude), float)

    def test_amenity_ids_attribute(self):
        """Test amenity_ids attribute"""
        new_place = self.value()
        self.assertEqual(type(new_place.amenity_ids), list)

    def test_reviews_relationship(self):
        """Test reviews relationship"""
        new_place = self.value()
        self.assertTrue(hasattr(new_place, "reviews"))

    def test_amenities_relationship(self):
        """Test amenities relationship"""
        new_place = self.value()
        self.assertTrue(hasattr(new_place, "amenities"))

if __name__ == '__main__':
    unittest.main()
