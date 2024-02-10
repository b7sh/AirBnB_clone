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

    def all(FileStorage):
        return FileStorage.__objects

    def new(FileStorage, obj):
        FileStorage.__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(FileStorage):
        serilized_dict = {}
        try:
            for key in FileStorage.__objects.keys():
                serilized_dict[key] = FileStorage.__objects[key].to_dict()
            with open(FileStorage.__file_path, "w") as f:
                json.dump(serilized_dict, f)
        except FileNotFoundError:
            pass

    def reload(FileStorage):
        classes = {"BaseModel": BaseModel, "User": User, "City": City,
                   "Place": Place, "State": State, "Amenity": Amenity,
                   "Review": Review}
        try:
            with open(FileStorage.__file_path, "r") as f:
                deserilized_dict = json.load(f)
            for key, value in deserilized_dict.items():
                Base = value["__class__"]
                Base = classes[value["__class__"]]
                new_base = Base(**value)
                FileStorage.new(new_base)

        except FileNotFoundError:
            return
