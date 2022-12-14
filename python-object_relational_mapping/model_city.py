#!/usr/bin/python3
'''Defining a database 
   class with sql-alchemy
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()


class City(Base):
    '''A class defination of a table in the sql'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
