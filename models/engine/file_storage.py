#!/usr/bin/python3
"""Store objects"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
            'Amenity': Amenity,'Place': Place, 'Review': Review}


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""

    # string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
                return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            tmp = {}
            tmp.update(self.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file 
        (__file_path) exists ; otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)"""    
        try:
            tmp = {}
            with open(self.__file_path, 'r') as f:
                tmp = json.load(f)
            for key, val in tmp.items():
                self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def get(self, cls, id):
        """Return object based on class name and id"""
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for val in all_cls.values():
            if (val.id == id):
                return val

        return None

    def count(self, cls=None):
        """count objects in storage"""
        all_classes = classes.values()

        if not cls:
            count = 0
            for clas in all_classes:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(clas).values())

        return count
