#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from sqlalchemy.sql import text

metadata = Base.metadata

place_amenity = Table(
    'place_amenity',
    metadata,
    Column('place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, server_default=text("1"))

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities",
                                 overlaps="place_amenities")
    else:
        @property
        def reviews(self):
            """getter for reviews"""
            review_dict = models.storage.all(Review)
            place_reviews = []
            for review in review_dict.values():
                if review.place_id == self.id:
                    place_reviews.append(review)
            return place_reviews

        @property
        def amenities(self):
            """getter for amenities"""
            amenity_dict = models.storage.all(Amenity)
            place_amenities = []
            for amenity in amenity_dict.values():
                if amenity.id in self.amenity_ids:
                    place_amenities.append(amenity)
            return place_amenities
