from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)
from app.services.employee_service import EmployeeService

router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)


@router.post(
    "",
    response_model=EmployeeResponse
)
def create_employee(
        request: EmployeeCreate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    return EmployeeService.create(
        db,
        request
    )


@router.get(
    "",
    response_model=List[EmployeeResponse]
)
def get_all_employees(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    return EmployeeService.get_all(db)


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
        employee_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    return EmployeeService.get_by_id(
        db,
        employee_id
    )


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
        employee_id: int,
        request: EmployeeUpdate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    return EmployeeService.update(
        db,
        employee_id,
        request
    )


@router.delete(
    "/{employee_id}"
)
def delete_employee(
        employee_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    return EmployeeService.delete(
        db,
        employee_id
    )