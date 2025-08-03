from fastapi import FastAPI
from .database import SessionLocal, engine
from . import model


#TODO: this is temporary, need to use db migrations
model.Base.metadata.create_all(bind=engine)  
app = FastAPI()

@app.get("/")
def root():
    return {"stataus": 200,
        "message": "Welcome to Amtrak Price Tracker"}

@app.get("/health")
def heartbeat():
    return {"status": 200,
            "message": "Server is alive"}
