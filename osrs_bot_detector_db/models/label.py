from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Label(Base):
    __tablename__ = 'Labels'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    label = Column(String(50), unique=True, nullable=False)
