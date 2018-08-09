from model import Base, Vote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///votes.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_survey_info(student_name, student_year):
    vote_object = Vote(name=student_name, year=student_year)
    session.add(vote_object)
    session.commit()

def get_all_survey_info():
    all_info = session.query(Vote).all()
    return all_info