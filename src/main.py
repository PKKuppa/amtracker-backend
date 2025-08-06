from fastapi import FastAPI
from . import model
from .api.user_routes import router as user_router

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def root():
    return {"stataus": 200,
        "message": "Welcome to Amtrak Price Tracker"}

@app.get("/health")
def heartbeat():
    return {"status": 200,
            "message": "Server is alive"}
