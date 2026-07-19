from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel


class Student(BaseModel):
    __tablename__ = "students"

    student_id: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    department: Mapped[str] = mapped_column(
        String(100)
    )

    semester: Mapped[int]