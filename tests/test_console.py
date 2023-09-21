#!/usr/bin/python3
""" Test for console """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console"""

    def setUp(self):
        """Set up the HBNB console for testing"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down the HBNB console after testing"""
        self.console = None
        storage._FileStorage__objects = {}

    def test_create_command(self):
        """Test the 'create' command by creating a new object"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()

        self.assertIn("BaseModel.", output)
        self.assertIn("id", storage.all().keys())
        self.assertIsInstance(storage.all()["BaseModel." + output], dict)

    def test_show_command(self):
        """Test the 'show' command by showing an individual object"""
        obj = {"name": "TestObject"}
        obj_id = obj["id"]
        storage.new(obj)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()

        self.assertIn(str(obj), output)

    def test_destroy_command(self):
        """Test the 'destroy' command by destroying an object"""
        obj = {"name": "TestObject"}
        obj_id = obj["id"]
        storage.new(obj)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            output = f.getvalue().strip()

        self.assertEqual(output, "")
        self.assertNotIn(obj_id, storage.all().keys())

    def test_all_command(self):
        """Test the 'all' command by listing all objects of a class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()

        self.assertEqual(output, "[]")

        obj1 = {"name": "TestObject1"}
        obj2 = {"name": "TestObject2"}
        storage.new(obj1)
        storage.new(obj2)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()

        self.assertIn(str(obj1), output)
        self.assertIn(str(obj2), output)

    def test_count_command(self):
        """Test the 'count' command by counting objects of a class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            output = f.getvalue().strip()

        self.assertEqual(int(output), 0)

        obj1 = {"name": "TestObject1"}
        obj2 = {"name": "TestObject2"}
        obj3 = {"name": "TestObject3"}
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            output = f.getvalue().strip()

        self.assertEqual(int(output), 3)

    def test_update_command(self):
        """Test the 'update' command by updating an object"""
        obj = {"name": "TestObject"}
        obj_id = obj["id"]
        storage.new(obj)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj_id} name NewName")
            output = f.getvalue().strip()

        self.assertEqual(output, "")
        updated_obj = storage.all()["BaseModel." + obj_id]
        self.assertEqual(updated_obj["name"], "NewName")

if __name__ == '__main__':
    unittest.main()
