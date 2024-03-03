#!/usr/bin/python3
"""The console"""


import cmd  # importing the cmd module
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


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

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        classes = storage.defclass.keys()
        if arg not in classes:
            print("** class doesn't exist **")
            return
        new_instance = storage.defclass[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        Usage: show <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in storage.defclass:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        obj_id = arg_list[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Usage: destroy <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in storage.defclass:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        obj_id = arg_list[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        Usage: all <class_name> or all
        """
        if arg:
            class_name = arg.split()[0]
            if class_name not in storage.defclass:
                print("** class doesn't exist **")
                return
            instances = []
            for key, instance in storage.all().items():
                if key.startswith(class_name + "."):
                    instances.append(str(instance))
        else:
            instances = []
            for instance in storage.all().values():
                instances.append(str(instance))
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arg_list = arg.split()

        if len(arg_list) < 4:
            print("** not enough arguments **")
            return
        class_name = arg_list[0]
        if class_name not in storage.defclass:
            print("** class doesn't exist **")
            return
        obj_id = arg_list[1]
        all_objects = storage.all()
        key = "{}.{}".format(class_name, obj_id)
        if key not in all_objects:
            print("** no instance found **")
            return
        attribute_name = arg_list[2]
        if attribute_name == "id" or attribute_name == "created_at" or attribute_name == "updated_at":
            print("** cannot update reserved attribute **")
            return
        new_value = " ".join(arg_list[3:])
        if not new_value:
            print("** value missing **")
            return
        instance = all_objects[key]
        setattr(instance, attribute_name, new_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
