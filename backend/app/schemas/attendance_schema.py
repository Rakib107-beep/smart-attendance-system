from datetime import date, time, datetime

from pydantic import BaseModel, ConfigDict
from datetime import date, time, datetime

class AttendanceResponse(BaseModel):
    id: int
    employee_id: int
    attendance_date: date
    check_in: time | None
    check_out: time | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )