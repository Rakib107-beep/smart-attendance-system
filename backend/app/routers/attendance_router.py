from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.schemas.attendance_schema import AttendanceResponse
from app.services.attendance_service import AttendanceService

router = APIRouter(
    prefix="/api/v1/attendance",
    tags=["Attendance"],
    dependencies=[Depends(get_current_user)]
)


@router.post(
    "/check-in",
    response_model=AttendanceResponse
)
def check_in(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    return AttendanceService.check_in(
        db,
        current_user
    )
@router.post(
    "/check-out",
    response_model=AttendanceResponse
)
def check_out(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):
    return AttendanceService.check_out(
        db,
        current_user
    )