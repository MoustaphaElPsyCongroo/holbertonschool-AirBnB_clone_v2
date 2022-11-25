#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    user = relationship("User", back_populates="places",
                        cascade="all, delete")

    cities = relationship("City", back_populates="places",
                          cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review", back_populates="place", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Getter for the list of City instances corresponding to this
            state """
            from models import storage
            return [review for review in storage.all(Review).values()
                    if self.id == review.place_id]
