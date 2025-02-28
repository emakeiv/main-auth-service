import os
import jwt
import uuid
from datetime import datetime, timedelta, timezone

from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat import primitives, backends


def __get_key(key_name: str, type: str):
    key_path = os.path.join(os.path.dirname(__file__), ".", "keys", key_name)
    with open(key_path, "rb") as key_file:

        if type == "public":
            key = load_pem_x509_certificate(key_file.read())
        if type == "private":
            key = primitives.serialization.load_pem_private_key(
                key_file.read(), password=None
            )

    return key


def encode(id: str) -> dict:
    now = datetime.now(tz=timezone.utc)
    payload = {
        "iss": "https://pvb.auth.io",
        "sub": str(uuid.uuid4()),
        "aud": "http://127.0.0.1:8080/",
        "user_id": id,
        "iat": now.timestamp(),
        "exp": (now + timedelta(minutes=30)).timestamp(),
        "scope": "openid",
    }
    print(f"payload: {payload}")
    key = __get_key("private_key.pem", "private")
    
    return jwt.encode(payload=payload, key=key, algorithm="RS256")


def decode(token: str) -> dict:
    try:
        unverified_headers = jwt.get_unverified_header(token)
        certificate = __get_key("public_key.pem", "public")
        key = certificate.public_key()
        decoded = jwt.decode(
            token,
            key=key,
            algorithms=unverified_headers["alg"],
            audience="http://127.0.0.1:8080/",
        )
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
    except jwt.InvalidAudienceError:
        raise ValueError("Invalid audience")

    return decoded
