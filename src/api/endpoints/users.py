
from fastapi import APIRouter

router = APIRouter()

@router.get("api/health")
async def health_check():
    return {"message": "API is healthy"}

@router.post("/api/users")
async def create_user():
    return {"message": "user created successfully"}

@router.get("/api/users/profile")
async def get_user():
    return {"message": "user profile"}

@router.post("api/users/generate_otp")
async def generate_otp():
    return {"message": "otp generated successfully"}

@router.post("api/users/verify_otp")
async def verify_otp():
    return {"message": "otp verified successfully"}

@router.post("api/token")
async def generate_token():
    return {"message": "token generated successfully"}
