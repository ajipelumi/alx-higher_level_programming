#!/usr/bin/python3
""" Displays a state object from passed database. """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


if __name__ == '__main__':
    db_user = sys.argv[1]  # Stores user
    db_password = sys.argv[2]  # Stores user password
    db_name = sys.argv[3]  # Stores name of database
    state_name = sys.argv[4]  # Stores state name

    # Create engine and session
    call = f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}'
    engine = create_engine(call)  # Establish connection
    session = Session(engine)  # Establish conversation with database

    # Query database to display states object
    states = session.query(State).filter(State.name == state_name).first()
    if states is None:
        print('Not found')
    else:
        print(states.id)
