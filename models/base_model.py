#!/usr/bin/python3

import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4)
        self.create_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def __str__(self):
        return f"{[self.__class__.__name__]} {self.id} {self.__dict__}"
    
    def save(self):
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["create_at"] = self.create_at.isoformat()
        class_dict["update_at"] = self.update_at.isoformat()
        return class_dict
    