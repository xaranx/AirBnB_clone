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
    __file_path = 'file.json'
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
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key obj class name.id
        """
        name = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.__objects[name] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dic, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    from models.base_model import BaseModel
                    value = eval(value["__class__"])(**value)
                    # value = BaseModel(**value)
                    FileStorage.__objects[key] = value
                # FileStorage.objects = json.load(f)
        else:
            return
