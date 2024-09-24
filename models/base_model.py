#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue

                if k in ['created_at', 'updated_at'] and isinstance(v, str):
                    v = datetime.fromisoformat(v)

                    setattr(self, k, v)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        """Returns a string representation of the instance"""
        # cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        to_json = self.__dict__.copy()
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = self.created_at.isoformat()
        to_json['updated_at'] = self.updated_at.isoformat()
        return to_json
