#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
import os
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for a command-line interface."""

    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'Amenity',
               'Place', 'City', 'State', 'Review']
    cmds = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def __init__(self):
        """Initialize the HBNBCommand instance."""
        super().__init__()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (Ctrl+D)."""
        return True

    def emptyline(self):
        """Emptyline method to override the default behavior."""
        pass

    def precmd(self, arg):
        """Pre-command method to handle method names with class names."""
        parts = arg.split('(')
        if len(parts) == 2:
            cmd_name, params = parts
            class_name, method_name = cmd_name.split('.')
            return f"{method_name} {class_name} {params.strip(')')}"
        return arg

    def do_create(self, arg):
        """Create a new instance of a class and save it to JSON file."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]
        params = args[1:]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        class_dict = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'Amenity': Amenity, 'State': State, 'Review': Review
        }

        param_dict = {}
        for param in params:
            parts = param.split('=')
            if len(parts) == 2:
                key, value = parts
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('_', ' ').replace('\\"', '"')
                elif '.' in value:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                param_dict[key] = value

        new_instance = class_dict[class_name](**param_dict)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Show all instances of a class or all classes."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            instance_list = []
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                if obj_name == args[0]:
                    instance_list += [value.__str__()]
            print(instance_list)

    def do_update(self, arg):
        """Update an instance's attribute value."""
        if not arg:
            print("** class name missing **")
            return

        args = ""
        for argv in arg.split(','):
            args = args + argv

        arg_list = shlex.split(args)

        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                obj_n = objc.__class__.__name__
                obj_id = objc.id
                if obj_n == arg_list[0] and obj_id == arg_list[1].strip('"'):
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, arg_list[2], arg_list[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_count(self, class_name):
        """Count the instances of a class."""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            cls = k.split('.')
            if cls[0] == class_name:
                count = count + 1
        print(count)

    def do_help(self, arg):
        """Provide a description of a given command."""
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            topics = ", ".join(self.get_names())
            print("Documented commands (type help <topic>):")
            print("=" * 40)
            print(topics)
            print()

    def help_quit(self):
        """Provide help for the quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Provide help for the EOF command."""
        print("EOF command to exit the program (Ctrl+D)")

    def help_create(self):
        """Provide help for the create command."""
        print("Create a new instance of BaseModel and save it to JSON file.")

    def help_show(self):
        """Provide help for the show command."""
        print("Show the string representation of an instance.")

    def help_help(self):
        """Provide help for the help command."""
        print("Provides description of a given command")


if __name__ == '__main__':
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
    storage.reload()
    HBNBCommand().cmdloop()
    print()
