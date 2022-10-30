#!/usr/bin/python3
""" Command Line program for the AirBnB project"""
import sys
import cmd
from models import storage
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State

classes = {'BaseModel': BaseModel, 'User': User,
        'Amenity': Amenity, 'City': City, 'State': State,
        'Place': Place, 'Review': Review
}


class HBNBCommand(cmd.Cmd):
    """Main Class for the command line interface"""

    __class_allow = ["BaseModel", "User", "Place",
        "State", "City", "Amenity", "Review"]

    if (sys.__stdin__.isatty()):
        prompt = '(hbnb) '

    def precmd(self, line):
        """Function for precmd loop"""
        return super().precmd(line)

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    @classmethod
    def check_entitie(cls, arg):
        """Checks on entities to validate classname attributes and values"""
        if len(arg) == 0:
            print("** class name missing *")
            return -1

        arg_lst = split(arg)
        if arg_lst[0] in cls.__class_allow:
            if len(arg_lst) <= 1:
                print("** instance id missing **")
                return -1
            else:
                key = arg_lst[0] + "." + arg_lst[1]
                if key in storage.all():
                    return 0
                else:
                    print("** no instance found **")
                    return -1
        else:
            print("** class doesn't exist **")
            return -1

    @classmethod
    def check_attribute(cls, args):
        """Checks on args to validate classname attributes and values"""
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True

    def emptyline(self):
        """ Empty line not displaying anything """
        pass

    def help_EOF(self):
        """ Help for the EOF"""
        print("Usage: count <class_name>")

    def help_quit(self):
        """ Help for the quit cmd"""
        print("Quit command to exit the program\n")

    def do_help(self, arg):
        """ Execution of the Help cmd"""
        return super().do_help(arg)

    def do_EOF(self, arg):
        """ Execution of the EOF """
        print("")
        return True

    def do_quit(self, command):
        """ Execution of the quit command """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of new Object, saves it
        (to the JSON file) and prints the id
        """
        args = arg.split()
        if not self.check_entitie(args):
            return

        new_obj = classes[args[0]]()
        storage.new(new_obj)
        storage.save()
        print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if self.check_entitie(arg) == 0:
            lst_tmp = split(arg)
            key = lst_tmp[0] + "." + lst_tmp[1]
            print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if self.check_entitie(arg) == 0:
            lst_tmp = split(arg)
            key = lst_tmp[0] + "." + lst_tmp[1]
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        get_all_cpy = storage.all().copy()
        lst = []
        arg_split = split(arg)
        if arg_split[0] in self.__class_allow:
            for key, value in get_all_cpy.items():
                if key.split(".")[0] == arg_split[0]:
                    lst.append(str(get_all_cpy[key]))

            print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if self.check_entitie(arg) == 0:
            arg_lst = split(arg)
            if self.check_attribute(arg_lst) == 0:
                key = arg_lst[0] + "." + arg_lst[1]
                setattr(storage.all()[key], arg_lst[2], arg_lst[3])
                storage.all()[key].save()
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
