__author__ = 'Suraj'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Shelter, Puppy, Adopter, PuppyProfile

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
shelters = session.query(Shelter).all()

for shelter in shelters:
    print("{}, {}".format(shelter.name, shelter.current_occupancy))