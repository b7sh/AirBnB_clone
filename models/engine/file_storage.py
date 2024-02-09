#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    
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
           # new_dict = self.__objects
            for key in self.__objects.keys():
                serilized_dict[key] = self.__objects[key].to_dict()
            with open(self.__file_path, "w") as f:
                json.dump(serilized_dict, f)
        except FileNotFoundError:
            pass

    def reload(self):
        classes = {"BaseModel": BaseModel}
        try:
            with open(self.__file_path, "r") as f:
                deserilized_dict = json.load(f)
            for key, value in deserilized_dict.items():
                Base = value["__class__"] #base = "BaseMdel"
                Base = classes[value["__class__"]]
                new_base = Base(**value)
                self.new(new_base)

        except FileNotFoundError:
            return
