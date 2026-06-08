from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/notes/{note_id}")
def get_note(note_id: int):

    if note_id <= 0:

        raise HTTPException(
            status_code=400,
            detail="Invalid Note ID"
        )

    return {
        "id": note_id
    }