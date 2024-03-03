#!/usr/bin/python3
"""The console"""


import cmd  # importing the cmd module
import shlex # Divide una cadena en una lista tokens
import models
import re
import ast
import inspect
from models.user import User
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


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
