from datetime import datetime, time

from app.models.attendance import Attendance
from app.repositories.attendance_repository import AttendanceRepository
from app.exceptions.custom_exception import AttendanceException


class AttendanceService:

    @staticmethod
    def check_in(
            db,
            current_user
    ):
        today = datetime.now().date()

        attendance = AttendanceRepository.get_today_attendance(
            db,
            current_user.id,
            today
        )

        if attendance:
            raise AttendanceException(
                "You have already checked in today."
            )

        current_time = datetime.now().time()

        late_time = time(9, 15)

        late_status = (
            "LATE_IN"
            if current_time > late_time
            else "ON_TIME"
        )

        attendance = Attendance(
            employee_id=current_user.id,
            attendance_date=today,
            check_in=current_time,
            late_status=late_status
        )

        return AttendanceRepository.create(
            db,
            attendance
        )