#!/usr/bin/python3
""" Module to define base class"""
import uuid
from datetime import datetime


class BaseModel:
    """ this is a base class"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """instante to string """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """this updates time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """instance to dictionary format"""
        dictt = {}
        dictt.update(self.__dict__)
        dictt.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictt['created_at'] = self.created_at.isoformat()
        dictt['updated_at'] = self.updated_at.isoformat()
        return dictt
