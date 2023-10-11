#!/usr/bin/python3
"""
Storing Json representation of a python file
"""
import json
import os


class FileStorage:
    """
    Serializes and Deserializes JSON files
    """
<<<<<<< HEAD
    __file_path = "file.json"
=======
    __file_path = 'file.json'
>>>>>>> fb94b3a54c8c1c75695f4fab53d3602e12fe687c
    __objects = {}

    def __init__(self):
        """
        Instantiation of class FileStorage
        """
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key obj class name.id
        """
        name = obj.__class__.__name__ + '.' + str(obj.id)
        self.__objects[name] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        dic = {k: v.to_dict() for k, v in self.__objects.items()}

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dic, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for k, v in (json.load(f)).items():
                    from models.base_model import BaseModel
                    value = eval(v["__class__"])(**v)
                    # value = BaseModel(**value)
                    self.__objects[k] = value
                # FileStorage.objects = json.load(f)
        else:
            return
