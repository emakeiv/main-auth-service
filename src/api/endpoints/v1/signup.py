
from fastapi import (
      status,
      Request, 
      Depends, 
      Response,
      APIRouter, 
      HTTPException
)

from api.schemas.users import (
    UserSchema,
    UsersListSchema,
    UserResponseSchema
) 

from uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork
from services.user_operations import UserService
from services.exceptions import DuplicateEmailError
from api.dependencies import get_uow 

router = APIRouter(
    prefix="/signup",
    tags=["signup"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def signup(user: UserSchema, uow: DatabaseUnitOfWork = Depends(get_uow)):
    user_service = UserService(uow)
    try:
        new_user = user_service.create_user(**user.model_dump())
        return new_user
    except DuplicateEmailError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

