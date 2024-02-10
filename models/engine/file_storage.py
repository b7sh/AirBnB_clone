#!/usr/bin/python3
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
        return self.__objects

    def new(self, obj):
        self.__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        serilized_dict = {}
        try:
            for key in self.__objects.keys():
                serilized_dict[key] = self.__objects[key].to_dict()
            with open(self.__file_path, "w") as f:
                json.dump(serilized_dict, f)
        except FileNotFoundError:
            pass

    def reload(self):
        classes = {"BaseModel": BaseModel, "User": User, "City": City,
                   "Place": Place, "State": State, "Amenity": Amenity,
                   "Review": Review}
        try:
            with open(self.__file_path, "r") as f:
                deserilized_dict = json.load(f)
                for value in deserilized_dict.values():
                    Base = value["__class__"]
                    del value["__class__"]
                    # Base = classes[value["__class__"]]
                    # new_base = Base(**value)
                    self.new(eval(Base)(**value))

        except FileNotFoundError:
            return
