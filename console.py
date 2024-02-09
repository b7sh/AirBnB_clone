#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """the airbnb interrpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,\
        saves it (to the JSON file) and prints the id"""
        arg = args.split()
        if len(arg) <= 0:
            print("** class name missing **")
            return
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            Base = BaseModel()
            storage.new(Base)
            Base.save()
            print(Base.id)

    def do_show(self, args):
        """Prints the string
        representation of an instance\
        based on the class name and id.
        """
        arg = args.split()
        if len(arg) <= 0:
            print("** class name missing **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False

        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        storage.reload()
        obj_dict = storage.all()
        key = f"{arg[0]}.{arg[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return False
        print(obj_dict[f"{arg[0]}.{arg[1]}"])

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

        elif arg[0] != "BaseModel":
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
        if len(arg) > 0:
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
                return False
        storage.reload()
        all = storage.all()
        for string in all:
            print(all[string])

    def do_update(self, args):
        """Updates an instance based on the\
            class name and id by adding or updating attribute """
        arg = args.split()
        
        if len(arg) <= 0:
            print("** class name missing **")
            return False
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False
        elif len(arg) < 3:
            print("** attribute name missing **")
            return False
        elif len(arg) < 4:
            print("** value missing **")
            return False
        key = f"{arg[0]}.{arg[1]}"
        storage.reload()
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return False
        obj = obj_dict[key]
        setattr(obj, arg[2], arg[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()