from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.database import test_connection, engine
from app.models import *
from app.models.base_model import Base
from app.routers.student_router import router as student_router
from fastapi.exceptions import RequestValidationError
from app.exceptions.custom_exception import StudentNotFoundException, DuplicateStudentException, \
    InvalidCredentialsException
from app.exceptions.exception_handler import student_not_found_exception_handler, duplicate_student_exception_handler, \
    validation_exception_handler, invalid_credentials_exception_handler
from app.middleware.logging_middleware import logging_middleware
from app.routers.auth_router import router as auth_router


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
app.middleware("http")(logging_middleware)
app.include_router(student_router)
app.include_router(auth_router)

app.add_exception_handler(
    StudentNotFoundException,
    student_not_found_exception_handler
)

app.add_exception_handler(
    DuplicateStudentException,
    duplicate_student_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_exception_handler
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