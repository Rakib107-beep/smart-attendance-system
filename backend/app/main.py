from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.database import test_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    test_connection()
    yield


app = FastAPI(
    title="Smart Attendance API",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Attendance API"
    }


@app.get("/health")
def health():
    return {
        "status": "UP",
        "message": "Smart Attendance Backend Running"
    }