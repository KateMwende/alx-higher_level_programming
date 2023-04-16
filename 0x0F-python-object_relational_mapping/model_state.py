#!/usr/bin/python3
"""
class State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class states(Base):
    """Defines a class state to link to a table"""
    id = Column(Integer, unique=True, nullable=False, primary key=true)
    name = Column(String(128), nullable=False)
