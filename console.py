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

    def do_show(self, args):
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

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        my_args = args.partition(" ")
        cls_name = my_args[0]
        cls_id = my_args[1]

        if cls_id and ' ' in cls_id:
            cls_id = cls_id.lstrip()

        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not cls_id:
             print("** instance id missing **")
             return

        key = cls_name + '.' + cls_id
        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

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
            if arg not in HBNBCommand.classes:
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
        args = args.partition(' ')
        cls_name = args[0]
        cls_id = args[2]

        if cls_name and ' ' in cls_name:
            cls_name = cls_name.lstrp()

        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.classes: 
            print("** class doesn't exist **")
            return

        if cls_id and ' ' in cls_id:
            cls_id = cls_id.lstrip()

        if not cls_id:
            print("** instance id missing **")
            return

        #key from class and id
        key = cls_name + '.' + cls_id

        if key not in storage.all():
            print("** no instance found **")
            return
        # checks if args or kwargs
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for key, value in kwargs.items():
                args.append(key)
                args.append(value)
            else: #isolates args
                args = args[2]
                if args and args[0] is '\"': #checks for quoted args
                    closing_quote = args.find('\"', 1)
                    attr_name = args[1:closing_quote]
                    args = args[closing_quote + 1:]

                args = args.partition(' ')

                #if attr_name is not quoted
                if not attr_name  and args[0] is not ' ':
                    attr_name = args[0]

                #if value is quoted
                if args[2] and args[2][0] is '\"':
                    attr_val = args[2][1:args[2].find('\"', 1)]

                # if attr_val is not quoted
                if not attr_val and args[2]:
                    attr_val = args[2].partition(' ')[0]

                args = [attr_name, attr_val]

        # dictionary of current objects
        new_dict = storage.all()[key]

        #iterate attr_names and attr_vals
        for i, attr_name in enumerate(args):
            if (i % 2 == 0):
                attr_val = args[i + 1]
                if not attr_name:
                    print("** attribute name missing **")
                    return
                if not attr_val:
                    print("** value missing **")
                    return

                if attr_name in HBNBCommand.types:
                    attr_val = HBNBCommand.types[att_name](att_val)

                #update dict with name and val
                new_dict.__dict__.update({attr_name: attr_val})

            new_dict.save() #save to file

    def help_update(self):
        """help for update method"""
        print("updates object instance")
        print("Usage: update <class name> <id> <attribute name> <attribute value>\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
