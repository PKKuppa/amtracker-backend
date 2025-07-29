from fastapi import APIRouter
import backend.src.schemas as schemas

router = APIRouter()

@router.post("/tracker")
async def create_tracker(tracker: schemas.TrackerCreate, user_id: int):
    #TODO: database call to create
    pass

@router.patch("/tracker/activate/{tracker_id}")
async def change_tracker_active_status(status_update: schemas.TrackerActivate, tracker_id: int):
    pass

@router.patch("/tracker/{tracker_id}")
async def update_tracker(update: schemas.TrackerUpdate, tracker_id: int):
    pass