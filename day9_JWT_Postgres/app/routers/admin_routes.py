from fastapi import APIRouter, Depends
from app.core.roles import require_admin

router = APIRouter(
    tags=["Administration"]
)

@router.get(
    "/admin",
    summary="Admin Dashboard",
    description="Accessible only to administrators."
)
def admin_dashboard(
    current_user=Depends(require_admin)
):
    return {
        "message": "Welcome Admin"
    }