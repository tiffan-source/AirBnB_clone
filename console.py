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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
