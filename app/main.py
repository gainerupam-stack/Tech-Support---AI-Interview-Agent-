from fastapi import FastAPI
from api.interview import router

app = FastAPI(
    title="AI Interview Agent",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Backend is running!"
    }