from jose import jwt
from datetime import datetime,timedelta
from jose import JWTError
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

ALGORITHM = os.getenv(
    "ALGORITHM"
)

def create_token(username):

    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("DECODED:", payload)

        return payload

    except JWTError as e:

        print("JWT ERROR:", e)

        return None

# If you need a token with a role included, use this helper
def create_token_with_role(username, role="user"):
    payload = {
        "sub": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)