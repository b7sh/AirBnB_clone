import json

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        try:
            with open(self.__file_path, "r") as f:
                serilized_dict = json.load(f)
            new_dict = self.__objects
            for key in new_dict.keys():
                serilized_dict[key] = new_dict[key].to_dict()

            with open(self.__file_path, "w") as f:
                json.dump(serilized_dict, f)
        except FileNotFoundError:
            new_dict = self.__objects
            serilized_dict = {}
            for key in new_dict.keys():
                serilized_dict[key] = new_dict[key].to_dict()
            with open(self.__file_path, "w") as f:
                json.dump(serilized_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                deserilized_dict = json.load(f)
        
        except FileNotFoundError:
            return

