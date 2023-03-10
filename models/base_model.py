#!/usr/bin/python3
"""Base model defining all common attributes/methods for other classes"""


import models
import uuid
from datetime import datetime


format_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """re-create an instance with this dictionary representation
        <class 'BaseModel'> -> to_dict() -> <class 'dict'> ->
        <class 'BaseModel'> """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                        kwargs["created_at"], format_time)
            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                        kwargs["updated_at"], format_time)
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """string representation of BaseModel class"""
        return ("[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

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

    def delete(self):
        """deletes an instance from storage"""
        models.storage.delete(self)
