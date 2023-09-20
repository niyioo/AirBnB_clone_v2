#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    name = Column(String(128))
    email = Column(String(128))
    password = Column(String(128))
