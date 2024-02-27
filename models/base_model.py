#!/usr/bin/python3
"""BaseModel"""


from uuid import uuid4
from datetime import datetime
# The UUID module in Python helps us to create unique identifiers for objects
# The datetime module provides us with classes to manipulate dates and times


class BaseModel:
    """This class defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """__init__() method

        Args:
            args:
                Unused positional arguments.
            kwargs:
                Dictionary representation of an instance.

        Description:
            When initialized with a dictionary, let's have a
            way to create that instance, otherwise, we will be
            guided by our already shaped instance attributes.
        """
        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'update_at':
                    time_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time_obj)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """__str__() method

        Returns:
            Returns a string representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save() method

        Description:
            To update the updated_at attribute with the current
            date and time each time we make changes to our class instance.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict() method

        Description:
            Returns a dictionary containing all
            keys/values of __dict__the instance.
        """
        dict_object = self.__dict__.copy()

        dict_object['__class__'] = self.__class__.__name__
        dict_object['created_at'] = self.created_at.isoformat()
        dict_object['updated_at'] = self.updated_at.isoformat()

        return dict_object
