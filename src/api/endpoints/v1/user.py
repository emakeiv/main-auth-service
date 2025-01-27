
from fastapi import APIRouter

router = APIRouter(
      prefix="/users",
      tags=["/users"],
      responses={404: {"description": "Not found"}},
)

@router.get("/{user_id}")
async def get_user(user_id):
      return {"message": "user profile endpoint"}