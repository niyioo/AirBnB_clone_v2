#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ Amenity class to store Amenity information """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)