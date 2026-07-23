from datetime import date

from app.models import Attendance
from app.models.user import User

from app.models.employee_attendance import Attendance


class DashboardService:

    @staticmethod
    def get_dashboard(db, current_user):

        today = date.today()

        employee_count = db.query(User).count()

        present = (
            db.query(Attendance)
            .filter(
                Attendance.attendance_date == today
            )
            .count()
        )

        late = (
            db.query(Attendance)
            .filter(
                Attendance.attendance_date == today,
                Attendance.late_status == "LATE"
            )
            .count()
        )

        absent = employee_count - present

        attendance = (
            db.query(Attendance)
            .filter(
                Attendance.employee_id == current_user.id,
                Attendance.attendance_date == today
            )
            .first()
        )

        today_data = {
            "check_in": None,
            "check_out": None,
            "status": None,
            "working_hours": None
        }

        if attendance:

            today_data = {

                "check_in": (
                    attendance.check_in.strftime("%H:%M:%S")
                    if attendance.check_in
                    else None
                ),

                "check_out": (
                    attendance.check_out.strftime("%H:%M:%S")
                    if attendance.check_out
                    else None
                ),

                "status": attendance.attendance_status,

                "working_hours": (
                attendance.working_hours.split(".")[0]
                if attendance.working_hours
                else None
)

            }

        return {

            "employee_count": employee_count,

            "present": present,

            "late": late,

            "absent": absent,

            "today": today_data

        }