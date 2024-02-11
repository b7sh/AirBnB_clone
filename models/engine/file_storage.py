#!/usr/bin/python3
"""define file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """store information to json file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return: dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """save object in dictionary"""
        self.__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serilazition for json file"""
        serilized_dict = {}
        try:
            for key in self.__objects.keys():
                serilized_dict[key] = self.__objects[key].to_dict()
            with open(self.__file_path, "w") as f:
                json.dump(serilized_dict, f)
        except FileNotFoundError:
            pass

    def reload(self):
        """deserilazition for json file"""
        classes = {"BaseModel": BaseModel, "User": User, "City": City,
                   "Place": Place, "State": State, "Amenity": Amenity,
                   "Review": Review}
        try:
            with open(self.__file_path, "r") as f:
                deserilized_dict = json.load(f)
                for value in deserilized_dict.values():
                    class_name = value["__class__"]
                    class_object = classes[class_name]
                    new_object = class_object(**value)
                    self.new(new_object)

        except FileNotFoundError:
            return
