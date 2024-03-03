#!/usr/bin/python3
"""The console"""


import cmd  # importing the cmd module
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        print()
        return True

    def emptyline(self):
        """Empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
