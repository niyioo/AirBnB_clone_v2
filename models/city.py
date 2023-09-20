from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    id = Column(String(60), primary_key=True, nullable=False,
                default=str(uuid.uuid4()), unique=True)
    places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")
