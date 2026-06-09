from fastapi import FastAPI

app = FastAPI()


@app.post("/login")
def login():

    return {
        "access_token": "sample_token"
    }

users = {
    "akhil": "akhil123"
}

from fastapi import HTTPException


@app.post("/login")
def login(
    username: str,
    password: str
):

    if username not in users:

        raise HTTPException(
            status_code=401,
            detail="Invalid User"
        )

    if users[username] != password:

        raise HTTPException(
            status_code=401,
            detail="Wrong Password"
        )

    return {
        "message": "Login Success"
    }

@app.get("/protected")
def protected():

    return {
        "message": "Protected Route"
    }