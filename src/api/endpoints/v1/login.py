
from fastapi import (
    status,
    Request, 
    Depends,
    Response,
    APIRouter, 
    HTTPException
)

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from api.dependencies import get_uow 
from uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork
from services.crud.user_operations import UserService
from services.security.auth_operations import AuthService
from api.schemas.token import (
    TokenDataResponseSchema,
    TokenResponseSchema
)

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

@router.post("/")
async def login(
        request: Request, 
        data : OAuth2PasswordRequestForm = Depends(),
        uow: DatabaseUnitOfWork = Depends(get_uow)
    ):
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
        auth_service = AuthService(uow)
        user = auth_service.authenticate_user(data.username, data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing credentials",
                headers={"WWW-Authenticate:" "Bearer"}
            )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Authorization header format"
        )
    
   