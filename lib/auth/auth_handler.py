# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict

import jwt
# from decouple import config

# JWT_SECRET = config("secret")
# JWT_ALGORITHM = config("algorithm")

JWT_SECRET = "d47eb0378b7071d97ac7"
JWT_ALGORITHM = "HS256"

# function used for signing the JWT string
def signJWT(email: str) -> Dict[str, str]:
    payload = {
        "email": email,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}