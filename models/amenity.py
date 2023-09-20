#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ The Amenity class, contains amenity information """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship("Place", secondary=place_amenity,
                                       viewonly=False,
                                       back_populates="amenities",
                                       overlaps="amenities")
