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
        return ("[{:s}] (:s) {}".format(self.__class__.name__,self.id,
                                        self.__dict__))
