#!/usr/bin/python3
""" module for state """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models.base import Base
from os import getenv


class State(BaseModel, Base):
    """State class that inherits from BaseModel and Base"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """getter attribute that returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            city_list = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
