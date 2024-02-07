#!/usr/bin/python3
"""define the BaseModule class"""
import uuid
import datetime


class BaseModel:
    """this basemodel class for airbnb"""
    def __init__(self):
        """define attributes
        Attributes:
        id (str) : the unique number for user
        create_at (str) : the thime create at
        update_at (str) : the time update at
        """
        self.id = str(uuid.uuid4())
        self.create_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def __str__(self):
        """ print the representation of BaseModule
        Returns:
            str : [<class name>] (<self.id>) <self.__dict__>
        """
        return f"{[self.__class__.__name__]} {self.id} {self.__dict__}"

    def save(self):
        """update the update attribute time"""
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        """represent all instances as dictionary

        Returns:
            dict: instances dict
        """
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["create_at"] = self.create_at.isoformat()
        class_dict["update_at"] = self.update_at.isoformat()
        return class_dict
