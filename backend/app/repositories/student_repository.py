from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student_schema import StudentCreate


class StudentRepository:

    @staticmethod
    def create(db: Session, student: StudentCreate):
        db_student = Student(
            student_id=student.student_id,
            full_name=student.full_name,
            email=student.email,
            department=student.department,
            semester=student.semester,
        )

        db.add(db_student)
        db.commit()
        db.refresh(db_student)

        return db_student

    @staticmethod
    def get_all(db: Session):
        return db.query(Student).all()