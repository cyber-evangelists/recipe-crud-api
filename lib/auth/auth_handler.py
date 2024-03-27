# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict
import jwt
from dotenv import load_dotenv
import os 

load_dotenv()
JWT_SECRET = os.environ["secret"]
JWT_ALGORITHM = os.environ["algorithm"]

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
    


    
    