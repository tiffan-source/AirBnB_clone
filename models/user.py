#!/usr/bin/python3
"""User Base Model"""
from models.base_model import BaseModel


class User(BaseModel):
    """Initialization of a User with its attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
