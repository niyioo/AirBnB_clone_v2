#!/usr/bin/python3
""" Module for testing DB storage"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class TestDBStorage(unittest.TestCase):
    """ Class to test the DB storage """

    @classmethod
    def setUpClass(cls):
        """ Set up test environment """
        os.environ['HBNB_ENV'] = 'test'
        cls.db = DBStorage()
        cls.db.reload()

    @classmethod
    def tearDownClass(cls):
        """ Remove storage file at the end of tests """
        del os.environ['HBNB_ENV']

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(self.db.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        self.db.new(new)
        self.assertIn(new, self.db.all().values())

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = self.db.all()
        self.assertIsInstance(temp, dict)

    def test_save(self):
        """ Save method works """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Reload method works """
        new = BaseModel()
        new.save()
        self.db.reload()
        for obj in self.db.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_delete(self):
        """ Delete method works """
        new = BaseModel()
        self.db.new(new)
        self.db.save()
        self.assertIn(new, self.db.all().values())
        self.db.delete(new)
        self.assertNotIn(new, self.db.all().values())

    def test_get(self):
        """ Test retrieving objects """
        new_user = User()
        self.db.new(new_user)
        new_state = State()
        self.db.new(new_state)
        self.db.save()
        self.assertEqual(new_user, self.db.get(User, new_user.id))
        self.assertEqual(new_state, self.db.get(State, new_state.id))

    def test_count(self):
        """ Test counting objects """
        self.assertEqual(0, self.db.count(BaseModel))
        new_user = User()
        self.db.new(new_user)
        self.db.save()
        self.assertEqual(1, self.db.count(User))
        new_state = State()
        self.db.new(new_state)
        self.db.save()
        self.assertEqual(1, self.db.count(User))
        self.assertEqual(1, self.db.count(State))

    def test_close(self):
        """ Test closing the session """
        self.db.close()
        self.assertEqual(None, self.db._DBStorage__session)


if __name__ == '__main__':
    unittest.main()
