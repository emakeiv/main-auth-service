import jwt
from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from jwt.exceptions import (
    ExpiredSignatureError,
    ImmatureSignatureError,
    InvalidAlgorithmError,
    InvalidAudienceError,
    InvalidKeyError,
    InvalidSignatureError,
    InvalidTokenError,
    MissingRequiredClaimError,
)

from src.services.security.token_utils import (
    encode,
    decode
)

UNPROTECTED_ROUTES = ["/signup","/signup/", "/login", "/docs", "/openapi.json"]

class AuthorizeRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        
        if any(request.url.path.startswith(route) for route in UNPROTECTED_ROUTES):
            print(f"✅ Allowed without auth: {request.url.path}")
            return await call_next(request)
        if request.method == "OPTIONS":
            return await call_next(request)
        
        bearer_token = request.headers.get("Authorization")
    
        if not bearer_token:
            print("❌ Missing access token")
            return Response(
                content='{"detail": "Missing access token"}',
                status_code=status.HTTP_401_UNAUTHORIZED,
                media_type="application/json",
            )
        
        try:
            auth_token = bearer_token.split(" ")[1].strip()
            token_payload = decode(auth_token)
            request.state.user_id = token_payload["sub"]
            
        except (
            ExpiredSignatureError,
            ImmatureSignatureError,
            InvalidAlgorithmError,
            InvalidAudienceError,
            InvalidKeyError,
            InvalidSignatureError,
            InvalidTokenError,
            MissingRequiredClaimError,
        ) as error:
            print(f"❌ Token validation error: {error}")
            return Response(
                content=f'{{"detail": "{str(error)}"}}',
                status_code=status.HTTP_401_UNAUTHORIZED,
                media_type="application/json",
            )
       