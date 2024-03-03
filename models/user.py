#!/usr/bin/python3
""" Create User """
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel"""
    password = ""
    email = ""
    first_name = ""
    last_name = ""