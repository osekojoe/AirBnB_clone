#!/usr/bin/python3
"""Store objects"""


import json


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""

    # string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
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
