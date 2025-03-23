
import os
from fastapi import APIRouter

router = APIRouter(
    tags=["root"]
)


@router.get("/")
async def home():
    return {"res": os.uname()}
