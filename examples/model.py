from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Vote(Base):
    __tablename__ = 'votes'
    vote_id = Column(Integer, primary_key=True)
    name = Column(String)
    animal = Column(String)

    def __repr__(self):
        return "{} likes {}.\n".format(self.name, self.animal)
