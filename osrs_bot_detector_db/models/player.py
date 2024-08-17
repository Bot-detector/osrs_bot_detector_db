from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Player(Base):
    __tablename__ = 'Players'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow)
    possible_ban = Column(Boolean, default=False)
    confirmed_ban = Column(Boolean, default=False)
    confirmed_player = Column(Boolean, default=False)
    label_id = Column(Integer, ForeignKey('Labels.id'))
    label_jagex = Column(Integer)
    ironman = Column(Boolean, default=False)
    hardcore_ironman = Column(Boolean, default=False)
    ultimate_ironman = Column(Boolean, default=False)
    normalized_name = Column(String)
