#!/usr/bin/python3
""" test base model"""
import unittest
import datetime
import json
import os
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """ Test cases for BaseModel class """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
        
    def setUp(self):
        """ Set up test environment """
        self.model = BaseModel()
        self.model.name = "Test"
        self.model.my_number = 42

    def tearDown(self):
        """ Remove test environment """
        storage._FileStorage__objects = {}
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ Test default instance """
        i = BaseModel()
        self.assertIsInstance(i, BaseModel)

    def test_kwargs(self):
        """ Test creating instance from dictionary """
        copy = self.model.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is self.model)
        self.assertEqual(new.id, self.model.id)
        self.assertEqual(new.name, self.model.name)
        self.assertEqual(new.my_number, self.model.my_number)
        self.assertEqual(new.created_at, self.model.created_at)
        self.assertEqual(new.updated_at, self.model.updated_at)

    def test_kwargs_int(self):
        """ Test invalid dictionary """
        copy = self.model.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Test save method """
        self.model.save()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], self.model.to_dict())

    def test_str(self):
        """ Test __str__ method """
        s = "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), s)

    def test_to_dict(self):
        """ Test to_dict method """
        self.assertEqual(type(self.model.to_dict()), dict)
        self.assertEqual(self.model.to_dict()['id'], self.model.id)
        self.assertEqual(self.model.to_dict()['name'], self.model.name)
        self.assertEqual(self.model.to_dict()['my_number'], self.model.my_number)
        self.assertEqual(
            self.model.to_dict()['created_at'], self.model.created_at.isoformat())
        self.assertEqual(
            self.model.to_dict()['updated_at'], self.model.updated_at.isoformat())

    def test_kwargs_none(self):
        """ Test invalid dictionary with None values """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """ Test invalid dictionary with one key """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)

    def test_id(self):
        """ Test id attribute """
        new = BaseModel()
        self.assertIsInstance(new.id, str)

    def test_created_at(self):
        """ Test created_at attribute """
        new = BaseModel()
        self.assertIsInstance(new.created_at, datetime.datetime)

    def test_updated_at(self):
        """ Test updated_at attribute """
        new = BaseModel()
        self.assertIsInstance(new.updated_at, datetime.datetime)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()
