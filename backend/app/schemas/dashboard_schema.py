from pydantic import BaseModel
from typing import Optional


class TodayAttendanceSchema(BaseModel):
    check_in: Optional[str]
    check_out: Optional[str]
    status: Optional[str]
    working_hours: Optional[str]


class DashboardResponse(BaseModel):
    employee_count: int
    present: int
    late: int
    absent: int
    today: TodayAttendanceSchema