

from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/generate_otp")
async def generate_otp():
    return {"message": "generatee otp  endpoint"}

@router.post("/verify_otp")
async def verify_otp():
    return {"message": "verify otp  endpoint"}

@router.post("/token")
async def generate_token():
    return {"message": "generate token endpoint"}