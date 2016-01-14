__author__ = 'Suraj'

import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Enum, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('adopter_id', Integer, ForeignKey('adopter.id')),
    Column('puppy_profile_id', Integer, ForeignKey('puppy_profile.id'))
)

class Shelter(Base):
    __tablename__ = 'shelter'

    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)
    city = Column(String(80), nullable=False)
    state = Column(String(80), nullable=False)
    zipcode = Column(Integer, nullable=False)
    website = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    maximum_capacity = Column(Integer, nullable=False)
    current_occupancy = Column(Integer, nullable=False)


class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    dateOfBirth = Column(Date, nullable=True)
    gender = Column(Enum('male', 'female'), nullable=False)
    weight = Column(Integer, nullable=False)
    picture = Column(String(250), nullable=True)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    puppy_profile = relationship("PuppyProfile", uselist=False, back_populates="puppy")


class PuppyProfile(Base):
    __tablename__ = "puppy_profile"

    id = Column(Integer, primary_key=True)
    profile_picture = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    special_needs = Column(String(1000), nullable=True)
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    puppy = relationship(Puppy, back_populates="puppy_profile")
    adopters = relationship("Adopter", secondary=association_table, back_populates="puppies")


class Adopter(Base):
    __tablename__ = "adopter"
    id = Column(Integer, primary_key=True)
    puppies = relationship("PuppyProfile", secondary=association_table, back_populates="adopters")


# insert at the end of the file
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)