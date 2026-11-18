from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/notes", tags=["notes"])
_notes: dict[int, str] = {}


class NoteIn(BaseModel):
    text: str = Field(min_length=1, max_length=500)


@router.post("", status_code=201)
def create_note(note: NoteIn) -> dict:
    note_id = len(_notes) + 1
    _notes[note_id] = note.text
    return {"id": note_id, "text": note.text}


@router.get("/{note_id}")
def get_note(note_id: int) -> dict:
    if note_id not in _notes:
        raise HTTPException(status_code=404, detail="note not found")
    return {"id": note_id, "text": _notes[note_id]}
