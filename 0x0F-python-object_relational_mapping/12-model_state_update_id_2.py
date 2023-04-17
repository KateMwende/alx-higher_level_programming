#!/usr/bin/python3
"""
Update a state with id of 2 to New Mexico
"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = craete_engine("mysql+mysqldb://{}:{}@localhost:3306:{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    stateUpdate = session.query(State).filter(State.id == 2).first()
    if stateUpdate:
        stateUpdate.name = 'New Mexico'
        session.commit()
