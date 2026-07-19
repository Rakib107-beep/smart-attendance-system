from sqlalchemy.orm import Session

from app.repositories.student_repository import StudentRepository
from app.schemas.student_schema import StudentCreate

from fastapi import HTTPException


class StudentService:

    @staticmethod
    def create_student(db: Session, student: StudentCreate):
        return StudentRepository.create(db, student)

    @staticmethod
    def get_students(db: Session):
        return StudentRepository.get_all(db)

    @staticmethod
    def get_student_by_id(db, student_id: int):
        student = StudentRepository.get_by_id(db, student_id)

        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found."
            )

        return student

    @staticmethod
    def update_student(db, student_id: int, student_data):
        student = StudentRepository.update(db, student_id, student_data)

        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found."
            )

        return student

    @staticmethod
    def delete_student(db, student_id: int):
        deleted = StudentRepository.delete(db, student_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Student not found."
            )

        return {
            "message": "Student deleted successfully."
        }