from sqlalchemy import Column, String

from app.models.base_model import BaseModel
from sqlalchemy import Enum
from app.models.enums.role import Role
from sqlalchemy.orm import relationship


class User(BaseModel):
    __tablename__ = "users"

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    full_name = Column(
        String(150),
        nullable=False
    )

    role = Column(
        Enum(Role),
        nullable=False,
        default=Role.USER
    )
    attendances = relationship(
        "Attendance",
        back_populates="employee",
        cascade="all, delete-orphan"
    )