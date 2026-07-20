from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String

from app.models.base_model import BaseModel


class Attendance(BaseModel):

    __tablename__ = "attendances"

    employee_id = Column(
        Integer,
        ForeignKey("users.id"),
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

    employee = relationship(
        "User",
        back_populates="attendances"
    )
    late_status = Column(
        String(20),
        nullable=False,
        default="ON_TIME"
    )