#!/usr/bin/python3
"""
define the base model class
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    class BaseModel
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *arg, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            from . import storage
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if not key == "__class__":
                    if key == "updated_at" or key == "created_at":
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)

    def __str__(self):
        """
        __str__ - return string representation of BaseModel instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save - updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        from . import storage
        storage.save()

    def to_dict(self):
        """
        to_dict - returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        rep = self.__dict__.copy()
        rep["__class__"] = self.__class__.__name__
        rep["created_at"] = self.created_at.isoformat()
        rep["updated_at"] = self.updated_at.isoformat()

        return rep
