#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute that returns the list of City instances with
            state_id equals to the current State.id (FileStorage)"""
            from models import storage
            return [city for city in storage.all("City").values()
                    if city.state_id == self.id]
