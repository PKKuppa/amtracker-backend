from fastapi import FastAPI
from fastapi import status
from . import model
from .api.user_routes import router as user_router
from .api.tracker_routes import router as tracker_router

app = FastAPI()
app.include_router(user_router)
app.include_router(tracker_router)

@app.get("/")
def root():
    return {"stataus": status.HTTP_200_OK,
        "message": "Welcome to Amtrak Price Tracker"}

@app.get("/health")
def heartbeat():
    return {"status": status.HTTP_200_OK,
            "message": "Server is alive"}
