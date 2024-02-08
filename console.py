#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


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
            base = BaseModel()
            base.save()
            print(base.id)

    def do_show(self, args):
        """Prints the string
        representation of an instance\
        based on the class name and id.
        """
        arg = args.split()
        if len(arg) <= 0:
            print("** class name missing **")
            return
        elif arg < 2:
            print("** instance id missing **")
            return

        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id\
            (save the change into the JSON file)
        """
        arg = args.split()
        if len(arg) <= 0:
            print("** class name missing **")
            return
        elif arg < 2:
            print("** instance id missing **")
            return

        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return

    def do_all(self, args):
        """rints all string representation of\
            all instances based or not on the class name.
        """
        arg = args.split()
        if len(arg) > 0:
            if arg[0] != "BaseModel":
                print("** class doesn't exist **")
                return
        all = BaseModel().all()
        print(all)

    def do_update(self, args):
        """Updates an instance based on the\
            class name and id by adding or updating attribute """
        arg = args.split()
        
        if len(arg) <= 0:
            print("** class name missing **")
            return
        elif arg < 2:
            print("** instance id missing **")
            return

        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
