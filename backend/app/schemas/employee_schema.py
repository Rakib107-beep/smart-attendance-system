from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr


class EmployeeBase(BaseModel):

    employee_code: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    department: str
    designation: str
    joining_date: date
    status: str = "ACTIVE"


class EmployeeCreate(EmployeeBase):
    username: str
    password: str


class EmployeeUpdate(BaseModel):

    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    department: str
    designation: str
    joining_date: date
    status: str


class EmployeeResponse(EmployeeBase):

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )