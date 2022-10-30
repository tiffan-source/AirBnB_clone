#!/usr/bin/python3
"""Review Base Model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Initialization of a Review with its attributes"""
    place_id = ""
    user_id = ""
    text = ""
