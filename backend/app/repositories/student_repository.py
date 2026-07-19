from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import desc, asc

from app.models.student import Student
from app.schemas.student_schema import StudentCreate
from sqlalchemy import or_


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
    def get_all(
            db,
            page: int = 1,
            size: int = 10,
            search: str = None,
            sort_by: str = "id",
            direction: str = "asc"
    ):
        query = db.query(Student)

        if search:
            query = query.filter(
                or_(
                    Student.student_id.ilike(f"%{search}%"),
                    Student.full_name.ilike(f"%{search}%"),
                    Student.email.ilike(f"%{search}%"),
                    Student.department.ilike(f"%{search}%")
                )
            )

        # Sorting
        if hasattr(Student, sort_by):
            column = getattr(Student, sort_by)

            if direction.lower() == "desc":
                query = query.order_by(desc(column))
            else:
                query = query.order_by(asc(column))

        skip = (page - 1) * size

        total = query.count()

        students = (
            query
            .offset(skip)
            .limit(size)
            .all()
        )

        return {
            "content": students,
            "page": page,
            "size": size,
            "total_elements": total,
            "total_pages": (total + size - 1) // size
        }

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

