#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """The Database engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the engine"""
        HBNB_ENV = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      getenv('HBNB_MYSQL_USER'),
                                      getenv('HBNB_MYSQL_PWD'),
                                      getenv('HBNB_MYSQL_HOST'),
                                      getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects currently stored in the
        database session, depending on name or not"""

        new_dict = {}

        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            for item in classes:
                result = self.__session.query(item).all()
                for element in result:
                    key = "{}.{}".format(item.__name__, element.id)
                    new_dict[key] = element
            return new_dict
        else:
            result = self.__session.query(cls).all()
            for element in result:
                key = "{}.{}".format(cls.__name__, element.id)
                new_dict[key] = element
            return new_dict

    def new(self, obj):
        """Adds an object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        "Creates all tables and session"
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        self.__session.close()
