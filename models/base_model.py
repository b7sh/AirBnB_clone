#!/usr/bin/python3
"""define the BaseModule class"""
import uuid
import datetime
import models


class BaseModel:
    """this basemodel class for airbnb"""
    def __init__(self, *args, **kwargs):
        """define attributes

        Attributes:
        id (str) : the unique number for user
        create_at (str) : the thime create at
        update_at (str) : the time update at
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.datetime.strptime(v, tformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """ print the representation of BaseModule
        Returns:
            str : [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the update attribute time"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """represent all instances as dictionary

        Returns:
            dict: instances dict
        """
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
