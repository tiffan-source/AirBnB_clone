#!/usr/bin/python3
""" Command Line program for the AirBnB project"""
import sys
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Main Class for the command line interface"""

    if (sys.__stdin__.isatty()):
        prompt = '(hbnb) '

    def emptyline(self):
        """ Empty line not displaying anything """
        pass

    def help_EOF(self):
        """ Help for the EOF"""
        print("Usage: count <class_name>")

    def help_quit(self):
        """ Help for the quit cmd"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """ Execution of the EOF """
        print()
        exit()

    def do_quit(self, command):
        """ Execution of the quit command """
        exit()

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if arg == "BaseModel":
                new_base_model = BaseModel()
                storage.new(new_base_model)
                storage.save()
                print(new_base_model.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if len(arg) == 0:
            print("** class name missing *")
        else:
            arg_lst = arg.split()
            if arg_lst[0] == "BaseModel":
                if len(arg_lst) <= 1:
                    print("** instance id missing **")
                else:
                    key = ".".join(arg_lst)
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if len(arg) == 0:
            print("** class name missing *")
        else:
            arg_lst = arg.split()
            if arg_lst[0] == "BaseModel":
                if len(arg_lst) <= 1:
                    print("** instance id missing **")
                else:
                    key = ".".join(arg_lst)
                    if key in storage.all():
                        del storage.all()[key]
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        get_all_cpy = storage.all().copy()
        lst = []

        if arg == "BaseModel":
            for key, value in get_all_cpy.items():
                if key.split(".")[0] == "BaseModel":
                    lst.append(str(get_all_cpy[key]))

            print(lst)
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
