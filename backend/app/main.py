from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from app.database.database import test_connection, engine
from app.models import *
from app.models.base_model import Base

from app.routers import dashboard_router
from app.routers.student_router import router as student_router
from app.routers.auth_router import router as auth_router
from app.routers.attendance_router import router as attendance_router
from app.routers.employee_router import router as employee_router

from app.exceptions.custom_exception import (
    StudentNotFoundException,
    DuplicateStudentException,
    InvalidCredentialsException,
    AttendanceException
)

from app.exceptions.exception_handler import (
    student_not_found_exception_handler,
    duplicate_student_exception_handler,
    validation_exception_handler,
    invalid_credentials_exception_handler,
    attendance_exception_handler
)

from app.middleware.logging_middleware import logging_middleware


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


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Middleware
app.middleware("http")(logging_middleware)


# Routers
app.include_router(
    dashboard_router.router,
    prefix="/api/v1"
)

app.include_router(student_router)
app.include_router(auth_router)
app.include_router(attendance_router)
app.include_router(employee_router)


# Exception handlers
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

app.add_exception_handler(
    AttendanceException,
    attendance_exception_handler
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