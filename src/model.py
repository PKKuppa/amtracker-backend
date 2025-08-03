
from sqlalchemy import Column, Integer, String, ForeignKey, Float
import uuid

from .database import Base

def generate_uuid():
    return uuid.uuid4()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, default=generate_uuid)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Tracker(Base):
    __tablename__ = "trackers"

    id = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    name = Column(String, index=True, nullable=False)
    departure_station = Column(String, index=True, nullable=False)
    arrival_station = Column(String, index=True, nullable=False)
    max_budget = Column(Float, nullable=False)
    is_active = Column(Integer, nullable=False)  # 0 or 1 for True and False