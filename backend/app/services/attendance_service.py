from datetime import datetime, time

from starlette.middleware.sessions import Session

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

    @staticmethod
    def check_out(db: Session, current_user):

        today = datetime.now().date()

        attendance = AttendanceRepository.get_today_attendance(
            db,
            current_user.id,
            today
        )

        if attendance is None:
            raise AttendanceException(
                "Please check in first."
            )

        if attendance.check_out is not None:
            raise AttendanceException(
                "You have already checked out today."
            )

        # Check Out Time Set
        attendance.check_out = datetime.now().time()

        # ===========================
        # Working Hours Calculation
        # ===========================

        check_in_datetime = datetime.combine(
            today,
            attendance.check_in
        )

        check_out_datetime = datetime.combine(
            today,
            attendance.check_out
        )

        duration = check_out_datetime - check_in_datetime

        attendance.working_hours = str(duration)

        # ===========================
        # Early Leave
        # ===========================

        office_end = time(18, 0)

        if attendance.check_out < office_end:
            attendance.early_leave_status = "YES"
        else:
            attendance.early_leave_status = "NO"

        return AttendanceRepository.update(
            db,
            attendance
        )