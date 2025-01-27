
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

router = APIRouter(
    prefix="/signup",
    tags=["signup"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserSchema, uow: DatabaseUnitOfWork = Depends(get_uow)):
    user_service = UserService(uow)
    try:
        new_user = user_service.create_user(**user.model_dump())
        return new_user
    except DuplicateEmailError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

