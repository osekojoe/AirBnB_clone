#!/usr/bin/python3
"""console - command interpreter"""


import cmd 


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
