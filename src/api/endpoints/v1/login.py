
from fastapi import (
    status,
    Request, 
    Depends,
    Response,
    APIRouter, 
    HTTPException
)
from api.dependencies import get_uow 
from uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork
from services.auth_operations import UserService
router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def login(request: Request, uow: DatabaseUnitOfWork = Depends(get_uow)):
    auth = request.headers.get("Authorization")
    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing credentials"
        )
    user_service = UserService(uow)

