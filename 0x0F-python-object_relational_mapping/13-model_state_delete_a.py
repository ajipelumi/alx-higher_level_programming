#!/usr/bin/python3
"""
Deletes all state objects with name containing
letter 'a' from passed database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


if __name__ == '__main__':
    db_user = sys.argv[1]  # Stores user
    db_password = sys.argv[2]  # Stores user password
    db_name = sys.argv[3]  # Stores name of database

    # Create engine and session
    call = f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}'
    engine = create_engine(call)  # Establish connection
    session = Session(engine)  # Establish conversation with database

    # Query database to filter state objects with letter 'a'
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        # Delete state objects
        session.delete(state)
    # Commit changes to database
    session.commit()
