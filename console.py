#!/usr/bin/python3
"""console - command interpreter"""


import sys
import cmd 
import models
from models.__init__ import storage
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


classes = {"BaseModel": BaseModel, 'User': User, 'State': State, 'City': City, 
            'Amenity': Amenity,'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """exit program"""
        return True

    def help_quit(self):
        """help for exit method"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """exit program"""
        return True

    def help_EOF(self):
        """help for EOF method"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel"""
        try:
            if not args:
                raise SyntaxError()
            my_args = args.split(' ')
            if my_args[0] not in classes:
                raise NameError()

            obj = eval("{}()".format(my_args[0]))
            for arg in my_args[1:]:
                if "=" not in arg:
                    continue
                attrs = arg.split("=")
                key = attrs[0]
                value = attrs[1]
                value = value.replace('_', ' ')
                setattr(obj, key, eval(value))
            obj.save()

            print("{}".format(obj.id))
        except NameError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")

    def help_create(self):
        """help for create method"""
        print("Creates a new instance of class")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234"""
        my_args = shlex.split(args)

        if len(my_args) == 0:
            print("** class name missing **")
            return
        if my_args[0] in classes:
            if len(my_args) > 1:
                key = my_args[0] + '.' + my_args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def help_show(self):
        """help for the show method"""
        print("Prints the string representation of an instance")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def help_destroy(self):
        """help for destroy method"""
        print("Deletes instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all """
        list_of_strings = []

        if args:
            arg = args.split(' ')[0]
            if arg not in classes:
                print("** class doesn't exist **")
                return

            for key, val in storage._FileStorage__objects.items():
                if key.split('.')[0] == arg:
                    list_of_strings.append(str(val))
        else:
            for key, val in storage._FileStorage__objects.items():
                list_of_strings.append(str(val))

        print(list_of_strings)

    def help_all(self):
        """help for all method"""
        print("Prints all string representation class instances")
        print("[Usage]: all <className>\n")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). 
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". """
        args = shlex.split(args)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def help_update(self):
        """help for update method"""
        print("updates object instance")
        print("Usage: update <class name> <id> <attribute name> <attribute value>\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
