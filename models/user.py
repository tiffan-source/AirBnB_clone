#!/usr/bin/python3
"""
module define User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User extends of BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
