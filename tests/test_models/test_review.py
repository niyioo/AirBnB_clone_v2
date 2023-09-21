#!/usr/bin/python3
"""Unit tests for Review class"""
import unittest
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """ Test Review Class """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_place_id_attribute(self):
        """Test place_id attribute"""
        new_review = self.value()
        self.assertEqual(type(new_review.place_id), str)

    def test_user_id_attribute(self):
        """Test user_id attribute"""
        new_review = self.value()
        self.assertEqual(type(new_review.user_id), str)

    def test_text_attribute(self):
        """Test text attribute"""
        new_review = self.value()
        self.assertEqual(type(new_review.text), str)


if __name__ == '__main__':
    unittest.main()
