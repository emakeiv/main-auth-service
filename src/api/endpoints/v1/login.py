
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
from services.user_operations import UserService
from services.auth_operations import AuthService
from api.schemas.users import (
    UserSchema
)
router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def login(request: Request, uow: DatabaseUnitOfWork = Depends(get_uow)):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing credentials"
        )
    try:
        auth_type, credentials = auth_header.split(" ", 1)
        if auth_type.lower() != "bearer":
            raise ValueError("Invalid authorization type")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Authorization header format"
        )
    
   