#!/usr/bin/python3
"""Contains the FileStorage class"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """class meant to manage JSON file.

    Attributes:
        __file_path: default path to save JSON serializations to file
        __objects: dict of items with BaseModel.
    """
    __file_path = 'HBnB_objects.json'
    __objects = {}

    def __init__(self):
        pass

    def all(self, cls=None):
        """Returns a dictionary of all objects or all objects of a specific class."""
        if cls is None:
            return self.__objects
        else:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}

    def new(self, obj):
        """Sets a new object as value in __objects with key '<object class name>.<object.id>'.

        Args:
            obj: BaseModel object to be added to __objects.
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file at __file_path into __objects."""
        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        class_dict = {c.__name__: c for c in classes}
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if content:
                    json_dict = json.loads(content)
                    for key, value in json_dict.items():
                        obj_class = class_dict[value['__class__']]
                        self.__objects[key] = obj_class(**value)

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
