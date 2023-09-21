#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")

    def __init__(self, *args, **kwargs):
        """Initialize City instance"""
        super().__init__(*args, **kwargs)
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            self.state_id = ""
            self.name = ""
