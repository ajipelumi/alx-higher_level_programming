#!/usr/bin/python3
""" Defines State class that inherits from Base. """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# ORM Model
Base = declarative_base()


class State(Base):
    """ State class that inherits from Base. """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade='all,delete',
                          backref='state')
