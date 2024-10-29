
from fastapi import APIRouter

router = APIRouter()

@router.get("api/is_alive")
async def is_alive():
    return {"message": "API is live"}

@router.post("/api/users")
async def create_user():
    return {"message": "create user endpoint"}

@router.get("/api/users/profile")
async def get_user():
    return {"message": "user profile endpoint"}

@router.post("api/users/generate_otp")
async def generate_otp():
    return {"message": "generatee otp  endpoint"}

@router.post("api/users/verify_otp")
async def verify_otp():
    return {"message": "verify otp  endpoint"}

@router.post("api/token")
async def generate_token():
    return {"message": "generate token endpoint"}
