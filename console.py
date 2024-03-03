#!/usr/bin/python3
"""The console"""


import cmd  # importing the cmd module
import shlex  # Divide una cadena en una lista tokens
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
    listOfProjectClass = ["BaseModel", "City", "Place", "Review", "State",
                          "User", "Amenity"]
    intAttrs = ["number_rooms", "number_bathrooms", "max_guest",
                "price_by_night"]
    floatAttrs = ["latitude", "longitude"]

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

    def do_create(self, arg):

        lineAsArgs = shlex.split(arg)
        if not self.verify_class_in_project(lineAsArgs):
            return
        newInstance = eval(str(lineAsArgs[0]) + '()')
        print(newInstance.id)
        newInstance.save()

    def do_show(self, arg):

        lineAsArgs = shlex.split(arg)
        if not self.verify_class_in_project(lineAsArgs):
            return
        if not self.verify_id_exists(lineAsArgs):
            return
        objectAsKey = str(lineAsArgs[0]) + '.' + str(lineAsArgs[1])
        objectsInStorage = models.storage.all()
        print(objectsInStorage[objectAsKey])

    def do_destroy(self, arg):

        lineAsArgs = shlex.split(arg)
        if not self.verify_class_in_project(lineAsArgs):
            return
        if not self.verify_id_exists(lineAsArgs):
            return
        objectAsKey = str(lineAsArgs[0]) + '.' + str(lineAsArgs[1])
        models.storage.all().pop(objectAsKey)
        models.storage.save()

    def do_all(self, arg):

        lineAsArgs = shlex.split(arg)
        objectsInStorage = models.storage.all()
        listOfObjectToPrint = []
        if len(lineAsArgs) == 0:
            for value in objectsInStorage.values():
                listOfObjectToPrint.append(str(value))
        else:
            if not self.verify_class_in_project(lineAsArgs):
                return
            for (key, value) in objectsInStorage.items():
                if lineAsArgs[0] in key:
                    listOfObjectToPrint.append(str(value))
        print(listOfObjectToPrint)

    def do_update(self, line):
 
        lineArgs = shlex.split(line)
        ArgLineDict = None
        if not self.verify_class_in_project(lineArgs):
            return
        if not self.verify_id_exists(lineArgs):
            return
        objAsKey = str(lineArgs[0]) + '.' + str(lineArgs[1])
        if "{" in line:
            ArgLineDict = self.check_dictionary_exists(line)
        if ArgLineDict is None:
            if not self.verify_attribute_arguments(lineArgs):
                return
            self.set_Attribute_correctly(objAsKey, lineArgs[2], lineArgs[3])
        if isinstance(ArgLineDict, dict):
            for (key, value) in ArgLineDict.items():
                self.set_Attribute_correctly(objAsKey, key, value)
        models.storage.all()[objAsKey].save()

    @staticmethod
    def check_dictionary_exists(line):
        """ Method checks if update was passed a dictionary"""
        lineAsArgs = line.split("{")
        dictionaryInLine = "{" + lineAsArgs[1]
        try:
            typeDictionary = ast.literal_eval(dictionaryInLine)
        except SyntaxError:
            return None
        return (typeDictionary)

    @classmethod
    def set_Attribute_correctly(cls, objAsKey, key, value):
        """sets the attributes with the correcy casting"""
        if key in cls.intAttrs:
            setattr(models.storage.all()[objAsKey], key, int(value))
        elif key in cls.floatAttrs:
            setattr(models.storage.all()[objAsKey], key, float(value))
        else:
            setattr(models.storage.all()[objAsKey], key, value)

    def default(self, line):
        """
        will ensure input is recycled through to meet contracts
        outlined in DBC methods
        """
        listOfCmdMethods = {"show": self.do_show,
                            "create": self.do_create,
                            "update": self.do_update,
                            "destroy": self.do_destroy,
                            "all": self.do_all,
                            "count": self.count_instance}
        if "." not in line:
            print("*** unknown syntax: " + line)
            return
        if "(" not in line or ")" not in line[-1]:
            print(line + " *** missing parenthesis")
            return
        lineAsArgs = re.findall(r"(.*?)\.(.*?)\((.*?)\)", line)
        if len(lineAsArgs) == 0:
            print("*** unknown syntax: " + line)
            return
        if lineAsArgs[0][1] not in listOfCmdMethods:
            print("*** command: " + lineAsArgs[0][1] + " is not reccognised")
            return
        className = lineAsArgs[0][0]
        method = lineAsArgs[0][1]
        info = lineAsArgs[0][2]
        argumentString = self.create_argument_string(className, method, info)
        if argumentString is None:
            return
        listOfCmdMethods[method](argumentString)

    @staticmethod
    def create_argument_string(className, method, info):
        """ this method is used to create a compatible string argument"""
        argumentString = className + " "
        if "," in info:
            if "{" in info:
                InfoSplit = re.findall(r'(.*)(\{.*?\})$', info)
                if len(InfoSplit) == 0:
                    print("Incorrect dictionary syntax in " + info)
                    return (None)
                firstArgument = InfoSplit[0][0].replace(",", "")
                dictionaryInLine = InfoSplit[0][1]
                argumentString += firstArgument + dictionaryInLine
            else:
                argumentString += info.replace(",", "")
        else:
            argumentString += info
        return (argumentString)

    def help_count(self):
        print("")

    def count_instance(self, arg):
        """retrieves number of instances of a class"""
        count = 0
        instanceStorage = models.storage.all()
        arg = shlex.split(arg)
        for (key, value) in instanceStorage.items():
            if arg[0] in key:
                count += 1
        print(count)

    @classmethod
    def verify_class_for_default(cls, classNameToCheck):
        """verify that class being created is defined in the project
        """
        if classNameToCheck not in cls.listOfProjectClass:
            return False
        return True

    @classmethod
    def verify_class_in_project(cls, args):
        """verify that class being created is defined in the project
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in cls.listOfProjectClass:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def verify_id_exists(args):
        """verify that the ID being called exists"""
        if len(args) < 2:
            print("** instance id missing **")
            return False
        objects = models.storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False
        return True

    @staticmethod
    def verify_attribute_arguments(args):
        """verify the attribute argument was passed correctly
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
