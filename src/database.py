from dotenv import load_dotenv
import os
# from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in the environment variables."
                     " Please set it in the .env file.")

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(AsyncAttrs,DeclarativeBase):
    pass

async def get_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
