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
    __file_path = "file.json"
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
        FileStorage.__objects[(obj.__class__.__name__).id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        else:
            pass
