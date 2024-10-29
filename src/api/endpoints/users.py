
from fastapi import (
      APIRouter, 
      Depends, 
      Request, 
      Response,
      HTTPException
)
from fastapi import status

from src.api.schemas.users import (
    UserSchema,
    UsersListSchema,
    UserResponseSchema
) 

from src.uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork
from src.services.auth_operations import UserService
from src.services.exceptions import DuplicateEmailError
from src.api.dependencies import get_uow 

router = APIRouter()

@router.get("api/is_alive")
async def is_alive():
    return {"message": "API is live"}

@router.post("/api/users", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserSchema, uow: DatabaseUnitOfWork = Depends(get_uow)):
    user_service = UserService(uow)
    try:
        new_user = user_service.create_user(user)
        return new_user
    except DuplicateEmailError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/api/users/{user_id}")
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
