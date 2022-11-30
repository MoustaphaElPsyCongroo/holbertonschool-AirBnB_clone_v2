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
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        self.__engine = create_engine((
            f"mysql+mysqldb://"
            f"{HBNB_MYSQL_USER}:"
            f"{HBNB_MYSQL_PWD}@"
            f"{HBNB_MYSQL_HOST}/"
            f"{HBNB_MYSQL_DB}"),
            pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects currently stored in the
        database session, depending on name or not"""
        results = {}

        classes = {"City": City, "State": State,
                   "User": User, "Place": Place,
                   "Review": Review, "Amenity": Amenity}

        if cls is not None:
            for instance in self.__session.query(classes[cls]).all():
                key = f"{classes[cls].__name__}.{instance.id}"
                results[key] = instance
        else:
            for cl in classes.keys():
                for instance in self.__session.query(classes[cl]).all():
                    key = f"{classes[cl].__name__}.{instance.id}"
                    results[key] = instance

        return results

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
        self.__session.remove()
