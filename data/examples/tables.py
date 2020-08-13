""" Tables declaration """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# Base déclarative (mapping Class <-> Database)
Base = declarative_base()


class Animal(Base):
    """ Les animaux """
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<tables.Animal(id='%s', name='%s')>" % (self.id, self.name)
