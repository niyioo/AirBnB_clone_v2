#!/usr/bin/python3
""" parent class for airbnb """
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import storage

Base = declarative_base()


class BaseModel:
    """Defines all common attributes/methods for SQLAlchemy
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """initializes all attributes for SQLAlchemy
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
        else:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """returns class name, id, and attribute dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if v is not None}
        return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
        """updates last update time and saves to the database
        """
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """creates a new dictionary, adding a key and returning
        datetimes converted to strings
        """
        new_dict = self.__dict__.copy()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        for key, value in new_dict.items():
            if isinstance(value, datetime):
                new_dict[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def delete(self):
        """Deletes the current instance from the storage (models.storage)
        """
        storage.delete(self)
