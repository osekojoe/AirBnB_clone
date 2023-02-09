#!/usr/bin/python3
"""console - command interpreter"""


import sys
import cmd 
from models.__init__ import storage


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
            if my_args[0] not in HBNBCommand.classes:
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

    def show(self, args):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234"""
        my_args = args.partition(" ")
        cls_name = my_args[0]
        cls_id = my_args[2]

        if cls_id and ' ' in cls_id:
            cls_id = cls_id.lstrip()

        if not cls_name:
            print("** class name missing **")

        if not cls_name not in HBNBCommand.classes:
             print("** class doesn't exist **")
             return

        if not cls_id:
            print("** instance id missing **")
            return

       key = cls_name + '.' + cls_id
       try:
           print(storage._FileStorage__objects[key])
        except:
            print("** no instance found **")

    def help_show(self):
        """help for the show method"""
        print("Prints the string representation of an instance")
        print("[Usage]: show <className> <objectId>\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
