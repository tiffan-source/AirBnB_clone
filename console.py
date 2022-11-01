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

classes = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
           'City': City, 'State': State, 'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Main Class for the command line interface"""

    __class_allow = ["BaseModel", "User", "Place",
                     "State", "City", "Amenity", "Review"]

    __cmd_list = ["all", "count", "show", "destroy", "update"]

    if (sys.__stdin__.isatty()):
        prompt = '(hbnb) '

    def precmd(self, line):
        """Function for precmd loop"""
        _cmd = _cls = _id = _args = ''

        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]
            _cls = pline[:pline.find('.')]

            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.__cmd_list:
                raise Exception

            pline = pline[pline.find('(') + 1:pline.find(')')]

            if pline:
                pline = pline.partition(', ')
                _id = pline[0].replace('\"', '')
                pline = pline[2].strip()
                if pline:
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    @classmethod
    def check_entitie(cls, arg):
        """Checks on entities to validate classname attributes and values"""
        if len(arg) == 0:
            print("** class name missing **")
            return False

        arg_lst = split(arg)
        if arg_lst[0] in cls.__class_allow:
            if len(arg_lst) <= 1:
                print("** instance id missing **")
                return False
            else:
                key = arg_lst[0] + "." + arg_lst[1]
                if key in storage.all():
                    return True
                else:
                    print("** no instance found **")
                    return False
        else:
            print("** class doesn't exist **")
            return False

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

    def help_count(self):
        """ Help for the quit cmd"""
        print("Usage: count <class_name>")

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

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage.all().items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def do_create(self, arg):
        """
        Creates a new instance of new Object, saves it
        (to the JSON file) and prints the id
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        if not args[0] in self.__class_allow:
            print("** class doesn't exist **")
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
        if self.check_entitie(arg):
            lst_tmp = split(arg)
            key = lst_tmp[0] + "." + lst_tmp[1]
            print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if self.check_entitie(arg):
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

        if len(arg) == 0:
            for key, value in get_all_cpy.items():
                lst.append(str(get_all_cpy[key]))
            print(lst)
        else:
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
        if self.check_entitie(arg):
            arg_lst = split(arg)
            if self.check_attribute(arg_lst):
                key = arg_lst[0] + "." + arg_lst[1]
                setattr(storage.all()[key], arg_lst[2], arg_lst[3])
                storage.all()[key].save()
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
