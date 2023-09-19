#!/usr/bin/python3
"""This module defines the DBStorage class for database storage."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages the database storage using SQLAlchemy."""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new instance of DBStorage."""
        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST', default='localhost'),
                os.getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries objects based on the specified class using the
        current session.
        """
        cls_list = [User, State, City, Amenity, Place, Review]
        if cls is None:
            objects = {}
            for cls in cls_list:
                objects.update(
                    {obj.id: obj for obj in self.__session.query(cls)})
        else:
            objects = {obj.id: obj for obj in self.__session.query(cls)}
        return objects

    def new(self, obj):
        """Adds an object to the current session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits changes to the current session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates database tables and initializes a new session
        using the engine.
        """
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Closes the current session."""
        self.__session.close()
