from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    student_id: str
    full_name: str
    email: EmailStr
    department: str
    semester: int


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True