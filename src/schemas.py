from pydantic import BaseModel
from typing import Optional

class TrackerCreate(BaseModel):
    name: str
    departure_station: str
    arrival_station: str
    max_budget: float
    is_active: bool

class TrackerActivate(BaseModel):
    is_active: bool

class TrackerUpdate(BaseModel):
    name: Optional[str] = None
    departure_station: Optional[str] = None
    arrival_station: Optional[str] = None
    max_budget: Optional[float] = None
    is_active: Optional[bool] = None

class TrackerOut(BaseModel):
    id: int
    name: str
    departure_station: str
    arrival_station: str
    max_budget: float
    is_active: bool

    class Config:
        orm_mode = True

class UserSignup(BaseModel):
    name: str
    email: str
    password: str


