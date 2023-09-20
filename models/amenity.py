#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel):
    """ Amenity class to store Amenity information """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # Define the Many-To-Many relationship with Place
        place_amenities = relationship("Place", secondary="place_amenity")
