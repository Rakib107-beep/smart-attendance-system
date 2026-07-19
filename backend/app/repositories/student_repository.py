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

    @staticmethod
    def get_by_id(db, student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()

    @staticmethod
    def update(db, student_id: int, student_data):
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return None

        student.student_id = student_data.student_id
        student.full_name = student_data.full_name
        student.email = student_data.email
        student.department = student_data.department
        student.semester = student_data.semester

        db.commit()
        db.refresh(student)

        return student

    @staticmethod
    def delete(db, student_id: int):
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return False

        db.delete(student)
        db.commit()

        return True

    @staticmethod
    def get_by_student_id(db, student_id: str):
        return (
            db.query(Student)
            .filter(Student.student_id == student_id)
            .first()
        )

    @staticmethod
    def get_by_email(db, email: str):
        return (
            db.query(Student)
            .filter(Student.email == email)
            .first()
        )

