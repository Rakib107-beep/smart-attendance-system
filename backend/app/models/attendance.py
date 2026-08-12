from sqlalchemy import Column, Integer, Date, Time, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Attendance(BaseModel):

    __tablename__ = "attendances"

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    attendance_date = Column(
        Date,
        nullable=False
    )

    check_in = Column(
        Time,
        nullable=True
    )

    check_out = Column(
        Time,
        nullable=True
    )

    late_status = Column(
        String(20),
        nullable=False,
        default="ON_TIME"
    )

    early_leave_status = Column(
        String(20),
        nullable=False,
        default="NO"
    )

    working_hours = Column(
        String(20),
        nullable=True
    )

    attendance_status = Column(
        String(20),
        nullable=False,
        default="PRESENT"
    )

    employee = relationship(
        "Employee",
        back_populates="attendances"
    )