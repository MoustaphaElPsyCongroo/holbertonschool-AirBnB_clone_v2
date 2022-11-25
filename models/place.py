#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                      Column(
                          "place_id", String(60), ForeignKey("places.id")),
                      Column(
                          "amenity_id", String(60), ForeignKey("amenities.id"))
                      )


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

        amenities = relationship(
            "Amenity",
            back_populates="place_amenities",
            secondary="place_amenity",
            viewonly=False)
    else:
        @property
        def cities(self):
            """Getter for the list of City instances corresponding to this
            state """
            from models import storage
            return [review for review in storage.all(Review).values()
                    if self.id == review.place_id]

        @property
        def amenities(self):
            from models import storage
            return [amenity for amenity in storage.all(Amenity).values()
                    if self.id == amenity.id]

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
