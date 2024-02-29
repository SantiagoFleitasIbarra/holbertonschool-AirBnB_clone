#!/usr/bin/python3
"""FileStorage"""


from models.base_model import BaseModel
import json
# This imports the module base_model to use its base class "BaseModel".
# This imports the module json


class FileStorage():
    """That serializes instances to a JSON
    file and deserializes JSON file to instances."""


# __file_path = "file.json"  #  private class attribute
# __objects = {}  #  private class attribute

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
        self.__objects[f"{self.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """save() method

        Description:
            serialize __object to the json file
        """
        obj_dict = {}

        for key, value in self.__objects.items():
            pass

    def reload(self):
        """reload() method

        Description:
            deserializes the JSON file to __objects
        """
        pass
