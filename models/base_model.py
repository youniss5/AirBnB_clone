#!/usr/bin/python3
""" Module to define base class"""
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """ this is a base class"""
    def __init__(self, *args, **kwargs):
        """ Construct """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created' not in kwargs.keys():
                    self.created = datetime.now()
                if 'updated' not in kwargs.keys():
                    self.updated = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created = datetime.now()
            self.updated = self.created
            models.storage.new(self)

    def save(self):
        """this updates time when instance is changed"""
        self.updated = datetime.now()
        models.storage.save()

    def to_dict(self):
        """instance to dictionary format"""
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created'] = self.created.isoformat()
        aux_dict['updated'] = self.updated.isoformat()
        return aux_dict
    def __str__(self):
        """instante to string """
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

