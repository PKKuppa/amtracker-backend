from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"stataus": 200,
        "message": "Welcome to Amtrak Price Tracker"}

@app.get("/health")
def heartbeat():
    return {"status": 200,
            "message": "Server is alive"}