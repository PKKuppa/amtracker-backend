from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from ..schemas import UserSignup, UserOut
from ..model import User
from ..database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
router = APIRouter()


@router.post("/signup", response_model= UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(signup: UserSignup, db: AsyncSession = Depends(get_db)):
    res = await db.stream(select(User).where(User.email == signup.email))
    user_exists = await res.scalar_one_or_none()
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Invalid email or password")

    user = User(**signup.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user