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
    """Command processor"""

    prompt = "(hbnb) "
    classes = [
        'BaseModel', 'User', 'Amenity',
        'Place', 'City', 'State', 'Review'
    ]
    cmds = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the console using Ctrl+D"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            clsn = arg.split('.')
            cmdn = clsn[1].split('(')
            arguments = cmdn[1].split(')')
            if clsn[0] in HBNBCommand.classes and cmdn[0] in HBNBCommand.cmds:
                arg = cmdn[0] + ' ' + clsn[0] + ' ' + arguments[0]
        return arg

    def do_create(self, arg):
        """ Creates an instance according to a given class with parameters """

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
        """ Shows string representation of an instance passed """

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
        """ Deletes an instance passed """

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
        """ Prints string represention of all instances of a given class """

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
        """ Updates an instance based on the class name and id """

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
        """counts number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            cls = k.split('.')
            if cls[0] == class_name:
                count = count + 1
        print(count)

    def do_help(self, arg):
        """Display help information for commands."""
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            topics = ", ".join(self.get_names())
            print("Documented commands (type help <topic>):")
            print("=" * 40)
            print(topics)
            print()

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF command to exit the program (Ctrl+D)")

    def help_create(self):
        print("Create a new instance of BaseModel and save it to JSON file.")

    def help_show(self):
        print("Show the string representation of an instance.")

    def help_help(self):
        """ Prints help command description """
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
