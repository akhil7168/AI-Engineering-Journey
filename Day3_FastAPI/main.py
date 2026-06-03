from fastapi import FastAPI

app = FastAPI()

notes = []


@app.get("/")
def root():
    return {
        "message": "Notes API"
    }


@app.get("/notes")
def get_notes():
    return notes


@app.post("/notes")
def create_note(
    note: str
):
    notes.append(note)

    return {
        "message": "Note added"
    }