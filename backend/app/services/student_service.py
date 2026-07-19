from sqlalchemy.orm import Session

from app.repositories.student_repository import StudentRepository
from app.schemas.student_schema import StudentCreate


class StudentService:

    @staticmethod
    def create_student(db: Session, student: StudentCreate):
        return StudentRepository.create(db, student)

    @staticmethod
    def get_students(db: Session):
        return StudentRepository.get_all(db)