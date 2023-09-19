#!/usr/bin/python3
""" module for place """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from os import getenv

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """returns list of review instances with place_id"""
            from models import storage
            review_list = []
            for k, v in storage.all(Review).items():
                if v.place_id == self.id:
                    review_list.append(v)
            return review_list

        @property
        def amenities(self):
            """returns list of amenity instances with place_id"""
            from models import storage
            amenity_list = []
            for k, v in storage.all(Amenity).items():
                if v.place_id == self.id:
                    amenity_list.append(v)
            return amenity_list
