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
        try:
            os.remove('file.json')
        except:
            pass

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

    def test_invalid_create_command(self):
        """Test creating an object with invalid command syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            output = f.getvalue().strip()

        self.assertIn("syntax error", output)

    def test_invalid_show_command(self):
        """Test showing an object with invalid command syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()

        self.assertIn("syntax error", output)

    def test_invalid_destroy_command(self):
        """Test destroying an object with invalid command syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            output = f.getvalue().strip()

        self.assertIn("syntax error", output)

    def test_invalid_all_command(self):
        """Test listing objects with invalid command syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()

        self.assertIn("syntax error", output)

    def test_invalid_update_command(self):
        """Test updating an object with invalid command syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            output = f.getvalue().strip()

        self.assertIn("syntax error", output)

    def test_non_existing_class(self):
        """Test using a non-existing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create NonExistingClass")
            output = f.getvalue().strip()

        self.assertIn("class doesn't exist", output)

    def test_invalid_attribute_name(self):
        """Test updating an object with an invalid attribute name"""
        obj = {"name": "TestObject"}
        obj_id = obj["id"]
        storage.new(obj)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj_id} invalid_attr NewValue")
            output = f.getvalue().strip()

        self.assertIn("attribute doesn't exist", output)

    def test_batch_mode(self):
        """Test batch mode by running commands from a file"""
        with open("test_batch_commands.txt", "w") as batch_file:
            batch_file.write("create BaseModel\nshow BaseModel\n")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("batch_test test_batch_commands.txt")
            output = f.getvalue().strip()

        self.assertIn("BaseModel.", output)
        self.assertIn("name", output)

    def test_non_interactive_mode(self):
        """Test non-interactive mode by running a command with -n option"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("-n 'create BaseModel'")
            output = f.getvalue().strip()

        self.assertIn("BaseModel.", output)
        self.assertIn("id", storage.all().keys())

    def test_unknown_command(self):
        """Test entering an unknown command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            output = f.getvalue().strip()

        self.assertIn("Unknown command", output)

    def test_exit_command(self):
        """Test the 'quit' command to exit the console"""
        with self.assertRaises(SystemExit):
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("quit")

    def test_help_command(self):
        """Test the 'help' command to display available commands"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()

        self.assertIn("Available commands:", output)
        self.assertIn("create", output)
        self.assertIn("show", output)
        self.assertIn("destroy", output)
        self.assertIn("all", output)
        self.assertIn("update", output)
        self.assertIn("quit", output)
        self.assertIn("help", output)

    def test_complex_object_creation(self):
        """Test creating objects with complex attributes"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel name=\"Complex Object\" my_list=[1, 2, 3] my_dict={\"key\": \"value\"}")
            output = f.getvalue().strip()

        self.assertIn("BaseModel.", output)
        obj = storage.all()["BaseModel." + output]
        self.assertEqual(obj["name"], "Complex Object")
        self.assertEqual(obj["my_list"], [1, 2, 3])
        self.assertEqual(obj["my_dict"], {"key": "value"})

    def test_complex_object_update(self):
        """Test updating objects with complex attributes"""
        obj = {"name": "TestObject", "my_list": [4, 5, 6], "my_dict": {"new_key": "new_value"}}
        obj_id = obj["id"]
        storage.new(obj)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {obj_id} my_list[0] 10 my_dict[new_key] NewValue")
            output = f.getvalue().strip()

        self.assertEqual(output, "")
        updated_obj = storage.all()["BaseModel." + obj_id]
        self.assertEqual(updated_obj["my_list"], [10, 5, 6])
        self.assertEqual(updated_obj["my_dict"], {"new_key": "NewValue"})


if __name__ == '__main__':
    unittest.main()
