#!/usr/bin/python3
"""console - command interpreter"""


import cmd 


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """exit program"""
        return True

    def do_EOF(self, arg):
        """exit program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
