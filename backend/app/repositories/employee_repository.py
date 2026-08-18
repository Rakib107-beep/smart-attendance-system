from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate


class EmployeeRepository:

    @staticmethod
    def create(
            db: Session,
            request: EmployeeCreate,
            user_id: int
    ):
        employee = Employee(
            user_id=user_id,
            employee_code=request.employee_code,
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            phone=request.phone,
            department=request.department,
            designation=request.designation,
            joining_date=request.joining_date,
            status=request.status
        )

        db.add(employee)

        return employee

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Employee)
            .order_by(Employee.id.desc())
            .all()
        )

    @staticmethod
    def get_by_id(
            db: Session,
            employee_id: int
    ):

        return (
            db.query(Employee)
            .filter(Employee.id == employee_id)
            .first()
        )

    @staticmethod
    def get_by_employee_code(
            db: Session,
            employee_code: str
    ):

        return (
            db.query(Employee)
            .filter(Employee.employee_code == employee_code)
            .first()
        )

    @staticmethod
    def get_by_email(
            db: Session,
            email: str
    ):

        return (
            db.query(Employee)
            .filter(Employee.email == email)
            .first()
        )

    @staticmethod
    def update(
            db: Session,
            employee: Employee,
            request: EmployeeUpdate
    ):

        employee.first_name = request.first_name
        employee.last_name = request.last_name
        employee.email = request.email
        employee.phone = request.phone
        employee.department = request.department
        employee.designation = request.designation
        employee.joining_date = request.joining_date
        employee.status = request.status

        db.commit()
        db.refresh(employee)

        return employee

    @staticmethod
    def delete(
            db: Session,
            employee: Employee
    ):

        db.delete(employee)
        db.commit()