
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
from services.crud.user_operations import UserService
from services.security.auth_operations import AuthService
from services.crud.exceptions import DuplicateEmailError
from api.dependencies import get_uow 

router = APIRouter(
    prefix="/signup",
    tags=["signup"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def signup(user: UserSchema, uow: DatabaseUnitOfWork = Depends(get_uow)):
    user_service = UserService(uow)
    auth_service = AuthService(uow)
    try:
        new_user = user_service.create_user(**user.model_dump())
        jwt = auth_service.encode(new_user, False)
        
        decoded = auth_service.decode(jwt)
        print(f"decoded jwt: {decoded}")
        return new_user
    except DuplicateEmailError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

