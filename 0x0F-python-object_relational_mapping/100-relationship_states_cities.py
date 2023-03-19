#!/usr/bin/python3
""" Displays all city objects from passed database. """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    db_user = sys.argv[1]  # Stores user
    db_password = sys.argv[2]  # Stores user password
    db_name = sys.argv[3]  # Stores name of database

    # Create engine and session
    call = f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}'
    engine = create_engine(call)  # Establish connection
    Base.metadata.create_all(engine)  # Create tables
    session = Session(engine)  # Establish conversation with database

    # Define new objects
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    # Add and commit new objects
    session.add(new_state)
    session.add(new_city)
    session.commit()
