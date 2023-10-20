#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

# Create the place_amenity table for the Many-To-Many relationship
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), primary_key=True, nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)

        # Relationships
        city = relationship('City', backref='places', foreign_keys='Place.city_id')
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')

        # Define the Many-To-Many relationship with Amenity
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            back_populates='place_amenities'
        )

        amenity_ids = []

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        # Define a getter method for reviews in FileStorage
        def reviews(self):
            """Getter attribute for reviews in FileStorage"""
            import models
            return [review for review in models.storage.all(Review)
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute for amenities in FileStorage"""
            import models
            return [amenity for amenity in models.storage.all(Amenity)
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, object):
            """Setter attribute for amenities in FileStorage"""
            if (type(object) == Amenity):
                self.amenity_ids.append(object.id)
