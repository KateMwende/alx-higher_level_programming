#!/usr/bin/python3
"""
class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative.base()


class City(Base):
    """
    City class that inherits from Base of model_state
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
