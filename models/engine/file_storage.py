#!/usr/bin/python3
"""Store objects"""


import json
import models


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
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file 
        (__file_path) exists ; otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                jsn = json.load(f)
            for key in jsn:
                self.__objects[key] = classes[jsn[key]["__class__"]](**jsn[key])
        except:
            pass
