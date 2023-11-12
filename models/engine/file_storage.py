#!/usr/bin/python3
"""module for class storage"""
import json
import uuid
import os


class FileStorage:
    """class to manage storage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """get the dict currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """define a new object added"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """this function to save dict to file"""
        with open(FileStorage.__file_path, 'w') as f:
            tem = {}
            tem.update(FileStorage.__objects)
            for key, val in tem.items():
                tem[key] = val.to_dict()
            json.dump(tem, f)

    def reload(self):
        """gets the storage from the file"""
        from models.base_model import BaseModel
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User
        from models.place import Place
        from models.state import State
        classes = {
                    'BaseModel': BaseModel, 'City': City, 'Amenity': Amenity,
                    'Review': Review, 'User': User, 'Place': Place,
                    'State': State
                  }
        try:
            tem = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in tem.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
