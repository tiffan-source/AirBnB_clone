#!/usr/bin/python3
"""
module file_storage define FileStorage class
"""
import json
from os.path import exists
from models.base_model import BaseModel


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
        dct_obj = {}
        dct_obj_convert = {}

        if exists(self.__file_path):
            with open(self.__file_path, "r") as file_objet:
                dct_obj = json.load(file_objet)

            for key, value in dct_obj.items():
                dct_obj_convert[key] = BaseModel(value)
            print(dct_obj)
            self.__objects = dct_obj_convert
