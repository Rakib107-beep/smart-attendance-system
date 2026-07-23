from datetime import date

from sqlalchemy.orm import Session

from app.models.user import User
from app.models.employee_attendance import Attendance


class DashboardRepository:

    @staticmethod
    def get_employee_count(db: Session):

        return db.query(User).count()

    @staticmethod
    def get_present_count(
            db: Session,
            today: date
    ):

        return (
            db.query(Attendance)
            .filter(
                Attendance.attendance_date == today
            )
            .count()
        )

    @staticmethod
    def get_late_count(
            db: Session,
            today: date
    ):

        return (
            db.query(Attendance)
            .filter(
                Attendance.attendance_date == today,
                Attendance.late_status == "LATE"
            )
            .count()
        )

    @staticmethod
    def get_today_attendance(
            db: Session,
            employee_id: int,
            today: date
    ):

        return (
            db.query(Attendance)
            .filter(
                Attendance.employee_id == employee_id,
                Attendance.attendance_date == today
            )
            .first()
        )