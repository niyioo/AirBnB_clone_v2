#!/usr/bin/python3
"""Unit tests for User class"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_first_name_attribute(self):
        """Test first_name attribute"""
        new_user = self.value()
        self.assertEqual(type(new_user.first_name), str)

    def test_last_name_attribute(self):
        """Test last_name attribute"""
        new_user = self.value()
        self.assertEqual(type(new_user.last_name), str)

    def test_email_attribute(self):
        """Test email attribute"""
        new_user = self.value()
        self.assertEqual(type(new_user.email), str)

    def test_password_attribute(self):
        """Test password attribute"""
        new_user = self.value()
        self.assertEqual(type(new_user.password), str)


if __name__ == '__main__':
    unittest.main()
