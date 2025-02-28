
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
from services.crud.user_operations import UserService
from services.security.auth_operations import AuthService
from api.schemas.token import (
    TokenDataResponseSchema,
    TokenResponseSchema
)
from api.schemas.login import (
       LoginRequestSchema
)

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def login(
        credentials: LoginRequestSchema, 
        uow: DatabaseUnitOfWork = Depends(get_uow)
    ):
    

        auth_service = AuthService(uow)
        user = auth_service.authenticate_user(
               credentials.reference, 
               credentials.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing credentials",
                headers={"WWW-Authenticate:" "Bearer"}
            )
        
        token = auth_service.generate_token(user)

        return {"access_token": token, "token_type": "bearer"}
   