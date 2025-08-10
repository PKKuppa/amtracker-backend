
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey
import uuid

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

class Base(AsyncAttrs,DeclarativeBase):
    pass

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, index=True, default=generate_uuid())
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

class Tracker(Base):
    __tablename__ = "trackers"

    id: Mapped[str] = mapped_column(primary_key=True, index=True, default=generate_uuid())
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    departure_station: Mapped[str] = mapped_column(index=True, nullable=False)
    arrival_station: Mapped[str] = mapped_column(index=True, nullable=False)
    max_budget: Mapped[float] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)