from sqlalchemy.orm import Session
from app.exceptions.custom_exception import StudentNotFoundException
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee_schema import (EmployeeCreate,EmployeeUpdate)
from app.models.user import User
from app.models.enums.role import Role
from app.auth.password import hash_password
from app.repositories.user_repository import UserRepository

from app.models.user import User
from app.models.enums.role import Role
from app.auth.password import hash_password
from app.repositories.user_repository import UserRepository


class EmployeeService:

    @staticmethod
    def create(
            db: Session,
            request: EmployeeCreate,
    ):

        # Employee code check
        if EmployeeRepository.get_by_employee_code(
                db,
                request.employee_code
        ):
            raise Exception(
                "Employee Code already exists."
            )

        # Employee email check
        if EmployeeRepository.get_by_email(
                db,
                request.email
        ):
            raise Exception(
                "Employee email already exists."
            )

        # Username check
        if UserRepository.get_by_username(
                db,
                request.username
        ):
            raise Exception(
                "Username already exists."
            )

        # User email check
        if UserRepository.get_by_email(
                db,
                request.email
        ):
            raise Exception(
                "User email already exists."
            )

        try:

            # 1. Create User
            user = User(
                username=request.username,
                full_name=(
                    f"{request.first_name} "
                    f"{request.last_name}"
                ),
                email=request.email,
                password=hash_password(request.password),
                role=Role.USER
            )

            db.add(user)

            # Get generated user.id
            db.flush()

            # 2. Create Employee
            employee = EmployeeRepository.create(
                db,
                request,
                user.id
            )

            # 3. Commit both User + Employee
            db.commit()

            # Refresh employee
            db.refresh(employee)

            return employee

        except Exception:
            db.rollback()
            raise

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