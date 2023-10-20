#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter attribute in case of file storage"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]

    def __init__(self, *args, **kwargs):
        """Initialize the State object"""
        super().__init__(*args, **kwargs)
