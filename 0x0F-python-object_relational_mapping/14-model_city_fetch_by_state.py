#!/usr/bin/python3
""" Displays all City object from passed database. """


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
import sys


if __name__ == '__main__':
    db_user = sys.argv[1]  # Stores user
    db_password = sys.argv[2]  # Stores user password
    db_name = sys.argv[3]  # Stores name of database

    # Create engine and session
    call = f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}'
    engine = create_engine(call)  # Establish connection
    session = Session(engine)  # Establish conversation with database

    # Query database to display City objects
    cities = session.query(City).join(State, City.state_id == State.id).all()
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')
