from fastapi import Depends, HTTPException, status

from auth import get_current_user
from database import SessionLocal
from models import User


def require_admin(current_user=Depends(get_current_user)):
    db = SessionLocal()

    db_user = (
        db.query(User)
        .filter(User.username == current_user["sub"])
        .first()
    )

    db.close()

    if db_user is None or db_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return db_user