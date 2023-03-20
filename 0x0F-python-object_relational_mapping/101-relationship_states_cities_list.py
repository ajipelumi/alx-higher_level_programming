#!/usr/bin/python3
""" Displays all State and corresponding City objects
from passed database.

"""
from sqlalchemy import create_engine
from sqlalchemy import asc
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
    session = Session(engine)  # Establish conversation with database

    # Query database to display all objects
    states = session.query(State)
    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print('\t'f'{city.id}: {city.name}')
