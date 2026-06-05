from sqlalchemy import create_engine, text

DATABASE_URL = (
    "postgresql://postgres:postgres123@localhost:5432/notes_db"
)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM notes")
    )

    for row in result:
        print(row)