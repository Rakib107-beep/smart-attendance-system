from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.database import test_connection, engine
from app.models import *
from app.models.base_model import Base
from app.routers.student_router import router as student_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    test_connection()
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Smart Attendance API",
    version="1.0.0",
    lifespan=lifespan
)

# Router Register
app.include_router(student_router)


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