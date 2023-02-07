#!/usr/bin/python3
"""Base model defining all common attributes/methods for other classes"""


import uuid
import datetime

class BaseModel:
    """defines all common attributes/methods for other classes"""
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        """string representation of BaseModel class"""
        return ("[{:s}] ({:s}) {}".format(self.__class__.__name__,self.id,
                                        self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ 
        of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__

        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()

        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()

        return new_dict
