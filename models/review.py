#!/usr/bin/python3
"""
module define Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review extends of BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
