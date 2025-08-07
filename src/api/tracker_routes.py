from fastapi import APIRouter, Depends
from fastapi import status,HTTPException
from ..schemas import TrackerCreate,TrackerOut
from ..schemas import TrackerActivate, TrackerUpdate
from ..model import Tracker
from ..database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/tracker",status_code=status.HTTP_201_CREATED, response_model=TrackerOut)
async def create_tracker(tracker_create: TrackerCreate, user_id: str, db : AsyncSession = Depends(get_db)):
    #TODO: limit num trackers
    tracker = Tracker(**tracker_create.model_dump(),user_id=user_id)
    db.add(tracker)
    await db.commit()
    await db.refresh(tracker)

    return tracker

@router.patch("/tracker/activate/{tracker_id}")
async def change_tracker_active_status(status_update: TrackerActivate, tracker_id: int):
    pass

@router.patch("/tracker/{tracker_id}")
async def update_tracker(update: TrackerUpdate, tracker_id: int):
    pass