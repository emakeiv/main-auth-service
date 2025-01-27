
from fastapi import APIRouter

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def login():
    return {"message": "login enpoint"}

