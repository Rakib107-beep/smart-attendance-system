from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.services.dashboard_service import DashboardService
from app.schemas.dashboard_schema import DashboardResponse

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "",
    response_model=DashboardResponse
)
def get_dashboard(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)

):

    return DashboardService.get_dashboard(
        db,
        current_user
    )