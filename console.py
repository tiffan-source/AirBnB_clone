#!/usr/bin/python3
""" Command Line program for the AirBnB project"""
import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Main Class for the command line interface"""

    __class_allow = ["BaseModel", "User"]

    if (sys.__stdin__.isatty()):
        prompt = '(hbnb) '

    @classmethod
    def check_entitie(cls, arg):
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
        Creates a new instance, saves it
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
            elif arg == "User":
                new_user = User()
                storage.new(new_user)
                storage.save()
                print(new_user.id)
            else:
                print("** class doesn't exist **")

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
            if len(arg_lst) == 2:
                print("** attribute name missing **")
            elif len(arg_lst) == 3:
                print("** value missing **")
            else:
                key = arg_lst[0] + "." + arg_lst[1]
                setattr(storage.all()[key], arg_lst[2], arg_lst[3])
                storage.all()[key].save()
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
