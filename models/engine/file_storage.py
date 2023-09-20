#!/usr/bin/python3
""" File storage for the airbnb """
import json
import os


class FileStorage:
    """ file storage class attributes """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects of a specific class if cls is
        provided, or all objects if cls is None.
        """
        if cls is not None:
            objects = {
                key: obj
                for key, obj in FileStorage.__objects.items()
                if isinstance(obj, cls)
            }
        else:
            objects = FileStorage.__objects
        return objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        data = {
            key: obj.to_dict()
            for key, obj in FileStorage.__objects.items()
        }

        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        cls = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'City': City, 'Amenity': Amenity, 'State': State,
            'Review': Review
        }

        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    data = json.load(file)
                    for key, value in data.items():
                        obj_class = value.get('__class__')
                        if obj_class in cls:
                            self.new(cls[obj_class](**value))
            except Exception as e:
                print(f"Error loading JSON file: {e}")

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside. If obj is equal to None,
        the method does nothing.
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()
