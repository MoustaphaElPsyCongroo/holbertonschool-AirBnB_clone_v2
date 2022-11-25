#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")

    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", back_populates="state",
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            """Getter for the list of City instances corresponding to this
            state """
            from models import storage
            return [city for city in storage.all(City).values()
                    if self.id == city.state_id]
