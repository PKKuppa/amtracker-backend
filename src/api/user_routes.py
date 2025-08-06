from fastapi import APIRouter, Depends
from ..schemas import UserSignup
from ..model import User
from ..database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter()


@router.post("/signup")
async def create_user(signup: UserSignup, db: AsyncSession = Depends(get_db)):
    test_user = UserSignup(**signup.model_dump())
    user = User(**signup.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user