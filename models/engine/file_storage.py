#!/usr/bin/python3
"""module for class storage"""
import json

class FileStorage:
    """ File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ objects to return  """
        return FileStorage.__objects

    def save(self):
        """ objects to json file """
        with open(FileStorage.__file_path, 'w') as f:
            tem = {}
            tem.update(FileStorage.__objects)
            for key, val in tem.items():
                tem[key] = val.to_dict()
            json.dump(tem, f)
      
    def new(self, obj):
         """ dictionary the object with a kye"""
         FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def reload(self):
        """ file to reload """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            tem = {}
            with open(FileStorage.__file_path, 'r') as f:
                tem = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

