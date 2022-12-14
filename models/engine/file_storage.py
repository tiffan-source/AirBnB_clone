#!/usr/bin/python3
"""
module file_storage define FileStorage class
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    class FileStorage - serializes instances to a JSON
    file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all -  returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        identifiant = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[identifiant] = obj

    def save(self):
        """
        save -  serializes __objects to the JSON file (path: __file_path)
        """
        dct_obj = {}

        for key, value in self.__objects.items():
            dct_obj[key] = value.to_dict()

        with open(self.__file_path, "w") as file_objet:
            json.dump(dct_obj, file_objet)

    def reload(self):
        """
        reload - deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing
        """
        classes = {
            'BaseModel': BaseModel, 'User': User,
            'Amenity': Amenity, 'City': City, 'State': State,
            'Place': Place, 'Review': Review
        }
        dct_obj = {}
        dct_obj_convert = {}

        if exists(self.__file_path):
            with open(self.__file_path, "r") as file_objet:
                try:
                    dct_obj = json.load(file_objet)
                except json.JSONDecodeError:
                    pass

            for key, value in dct_obj.items():
                dct_obj_convert[key] = classes[key.split('.')[0]](**value)

            self.__objects = dct_obj_convert
