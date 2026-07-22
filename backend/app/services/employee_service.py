from sqlalchemy.orm import Session

from app.exceptions.custom_exception import StudentNotFoundException
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate
)


class EmployeeService:

    @staticmethod
    def create(
            db: Session,
            request: EmployeeCreate
    ):

        if EmployeeRepository.get_by_employee_code(
                db,
                request.employee_code
        ):

            raise Exception(
                "Employee Code already exists."
            )

        if EmployeeRepository.get_by_email(
                db,
                request.email
        ):

            raise Exception(
                "Email already exists."
            )

        return EmployeeRepository.create(
            db,
            request
        )

    @staticmethod
    def get_all(
            db: Session
    ):

        return EmployeeRepository.get_all(db)

    @staticmethod
    def get_by_id(
            db: Session,
            employee_id: int
    ):

        employee = EmployeeRepository.get_by_id(
            db,
            employee_id
        )

        if not employee:

            raise StudentNotFoundException(
                "Employee not found."
            )

        return employee

    @staticmethod
    def update(
            db: Session,
            employee_id: int,
            request: EmployeeUpdate
    ):

        employee = EmployeeRepository.get_by_id(
            db,
            employee_id
        )

        if not employee:

            raise StudentNotFoundException(
                "Employee not found."
            )

        email = EmployeeRepository.get_by_email(
            db,
            request.email
        )

        if email and email.id != employee.id:

            raise Exception(
                "Email already exists."
            )

        return EmployeeRepository.update(
            db,
            employee,
            request
        )

    @staticmethod
    def delete(
            db: Session,
            employee_id: int
    ):

        employee = EmployeeRepository.get_by_id(
            db,
            employee_id
        )

        if not employee:

            raise StudentNotFoundException(
                "Employee not found."
            )

        EmployeeRepository.delete(
            db,
            employee
        )

        return {
            "message": "Employee deleted successfully."
        }