#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", back_populates="state",
                              cascade="all, delete")
    else:
        @property
        def places(self):
            """Getter for the list of City instances corresponding to this
            state """
            from models import storage
            return [place for place in storage.all(Place).values()
                    if self.id == place.state_id]
