#!/usr/bin/python3
"""module for class storage"""
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ objects to return  """
        return FileStorage.__objects
    def reload(self):
        """ file to reload """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, val in l_json.items():
                    FileStorage.__objects[key] = eval(
                        val['__class__'])(**val)
    def save(self):
        """ objects to json file """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, fname)
      
    def new(self, obj):
         """ dictionary the object with a kye"""
         FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

