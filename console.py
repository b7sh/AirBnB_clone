#!/usr/bin/python3
"""define console module"""
import re
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the airbnb interrpreter"""
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel(), "User": User(), "City": City(),
               "Place": Place(), "State": State(), "Amenity": Amenity(),
               "Review": Review()}

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,\
        saves it (to the JSON file) and prints the id"""
        arg = args.split()
        if len(arg) <= 0:
            print("** class name missing **")
            return False
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        else:
            Base = self.classes[arg[0]]
            storage.new(Base)
            Base.save()
            print(Base.id)

    def do_show(self, args):
        """Prints the string
        representation of an instance
        based on the class name and id.
        """
        arg = args.split()
        if len(arg) <= 0:
            print("** class name missing **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False

        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        storage.reload()
        obj_dict = storage.all()
        key = f"{arg[0]}.{arg[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return False
        print(obj_dict[key])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id\
            (save the change into the JSON file)
        """
        arg = args.split()
        if len(arg) <= 0:
            print("** class name missing **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False

        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        storage.reload()
        obj_dict = storage.all()
        key = f"{arg[0]}.{arg[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return False
        del obj_dict[key]
        storage.save()

    def do_all(self, args):
        """rints all string representation of\
            all instances based or not on the class name.
        """
        arg = args.split()
        storage.reload()
        all = storage.all()
        if len(arg) > 0:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
                return False
            else:
                object_list = []
                for value in all.values():
                    if value.__class__.__name__ == arg[0]:
                        object_list.append(str(value))
                        print(object_list)

        else:
            k = []
            j = []
            for key in all.keys():
                k.append(key)
            for key in k:
                j.append(str(all[key]))
            print(j)

    def do_update(self, args):
        """Updates an instance based on the\
            class name and id by adding or updating attribute """
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        elif len(arg) <= 1:
            print("** instance id missing **")
            return False
        elif len(arg) <= 2:
            print("** attribute name missing **")
            return False
        elif len(arg) <= 3:
            print("** value missing **")
            return False
        key = f"{arg[0]}.{arg[1]}"
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return False

        attr_name = arg[2]
        attr_value = arg[3]
        obj = storage.all()[key]

        if attr_name in obj.__class__.__dict__.keys():
            attr_type = type(obj.__class__.__dict__[attr_name])

            if attr_type == dict:
                value_dict = eval(attr_value)
                obj.__dict__[attr_name].update(value_dict)
            else:
                obj.__dict__[attr_name] = attr_type(attr_value)
        else:
            obj.__dict__[attr_name] = attr_value

        storage.save()

    def do_count(self, args):
        """the number of things"""
        count = 0
        arg = args.split()
        if arg[0] in self.classes.keys():
            objects = storage.all()
            for value in objects.values():
                if value.__class__.__name__ == arg[0]:
                    count += 1
        print(count)

    def precmd(self, line):
        pattern = re.search(r"(\w+)\.(\w+)\(\)", line)
        if pattern:
            class_ = pattern.group(1)
            func = pattern.group(2)
            command = func + " " + class_
            return command
        else:
            return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
