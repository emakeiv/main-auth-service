from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)

@router.get("/is_alive")
async def is_alive():
    return {"message": "API is live"}
