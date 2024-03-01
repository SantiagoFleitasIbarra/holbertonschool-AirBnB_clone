#!/usr/bin/python3
"""FileStorage"""


from models.base_model import BaseModel
import json
# This imports the module base_model to use its base class "BaseModel".
# This imports the module json


class FileStorage():
    """That serializes instances to a JSON
    file and deserializes JSON file to instances."""

    __file_path = "file.json"  # private class attribute
    __objects = {}  # private class attribute

    def all(self):
        """all() method

        Return:
            Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """new() method

        Description:
            sets in __objects the obj
        """
        key = "{}.{}".format(self.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save() method

        Description:
            serialize __object to the json file
        """
        with open(FileStorage.__file_path, "w") as file:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, file)

    def reload(self):
        """reload() method

        Description:
            deserializes the JSON file to __objects
        """

        # Defclass dictionary to contain all user-defined classes to
        # be used to recreate class instances (objects).
        defclass = {
            'BaseModel': BaseModel
            }

        try:
            with open(FileStorage.__file_path, "r") as file:
                deserialized = json.load(file)
                for key, value in deserialized.items():
                    classname = value["__class__"]
                    if classname in defclass:
                        classobj = defclass[classname]
                        self.new(classobj(**value))
        except FileNotFoundError:
            return
