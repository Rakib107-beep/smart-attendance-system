from datetime import datetime

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.exceptions.custom_exception import StudentNotFoundException, DuplicateStudentException


async def student_not_found_exception_handler(
        request: Request,
        exc: StudentNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "timestamp": datetime.now().isoformat(),
            "status": 404,
            "error": "Not Found",
            "message": exc.message,
            "path": request.url.path
        }
    )

async def duplicate_student_exception_handler(
        request: Request,
        exc: DuplicateStudentException
):
    return JSONResponse(
        status_code=409,
        content={
            "timestamp": datetime.now().isoformat(),
            "status": 409,
            "error": "Conflict",
            "message": exc.message,
            "path": request.url.path
        }
    )

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = []

    for error in exc.errors():
        errors.append({
            "field": ".".join(str(x) for x in error["loc"][1:]),
            "message": error["msg"]
        })

    return JSONResponse(
        status_code=422,
        content={
            "timestamp": datetime.now().isoformat(),
            "status": 422,
            "error": "Validation Error",
            "message": errors,
            "path": request.url.path
        }
    )