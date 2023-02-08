#!/usr/bin/python3
<<<<<<< HEAD

""" Engine package for the AirBnB """
import json
from os import path

class FileStorage:
    """Class that serializes instances to a JSON file and deserializes JSON file to instances"""

     # Path to the JSON file
    __file_path = "file.json"
    # Dict to store the objects
    __objects = {}

    
    def all(self):
        """ 
        all(self): returns the dictionary __objects
        """
        return FileStorage.__objects

        def new(self, obj):
            """
            new(self, obj): sets in __objects the obj with key <obj class name>.id
            """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

        def save(self):
            """
            save(self): serializes __objects to the JSON file (path: __file_path)
            """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)
            

            def reload(self):
                """
                reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file does not exist, no exception should be raised)
                """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = {key: obj.__class__(**value)
                                         for key, value in json.load(f).items()}
        except FileNotFoundError:
            pass


=======
""" """
>>>>>>> 9a6616c2a7903dc8752751545513c57c5c14cdc8
