from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.student_schema import StudentCreate, StudentResponse
from app.services.student_service import StudentService
from fastapi import Query

router = APIRouter(
    prefix="/api/v1/students",
    tags=["Students"]
)


@router.post("/", response_model=StudentResponse)
def create_student(
        student: StudentCreate,
        db: Session = Depends(get_db)
):
    return StudentService.create_student(db, student)


@router.get("/")
def get_students(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    search: str | None = None,
    sort_by: str = "id",
    direction: str = "asc",
    db: Session = Depends(get_db)
):
    return StudentService.get_students(
        db,
        page,
        size,
        search,
        sort_by,
        direction
    )

@router.get("/{student_id}")
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    return StudentService.get_student_by_id(db, student_id)

@router.put("/{student_id}")
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return StudentService.update_student(db, student_id, student)

@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return StudentService.delete_student(db, student_id)