from datetime import date

from sqlalchemy.orm import Session

from app.models.attendance import Attendance


class AttendanceRepository:

    @staticmethod
    def get_today_attendance(
            db: Session,
            employee_id: int,
            attendance_date: date
    ):
        return (
            db.query(Attendance)
            .filter(
                Attendance.employee_id == employee_id,
                Attendance.attendance_date == attendance_date
            )
            .first()
        )

    @staticmethod
    def create(
            db: Session,
            attendance: Attendance
    ):
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        return attendance

    @staticmethod
    def update(
            db: Session,
            attendance: Attendance
    ):
        db.commit()
        db.refresh(attendance)
        return attendance