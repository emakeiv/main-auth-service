
import jwt
import uuid
from  datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dal.models.user import User
from env_configuration import get_settings
from services.crypto.common_utils import match_password
from uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

class AuthService():
      def __init__(self, uow: DatabaseUnitOfWork):
                self.uow = uow
                self.settings = get_settings() 
        
      def authenticate_user(self, reference: str, password:str) -> User:
            with self.uow as uow:      
                  user = uow.repos.get(reference) 
                  if not user:
                        raise ValueError("Invalid email or password")                       
                  if not match_password(password, user.password):
                        raise ValueError("Invalid email or password")                        
                  return user

      def encode(self, user:User, admin:bool):
            now = datetime.now(tz=datetime.timezone.utc)
            payload = {
                  "sub": str(uuid.uuid4()),
                  "aud": "http://127.0.0.1:8080/",
                  "user_id": user.user_id,
                  "iat": now.timestamp(),
                  "exp": now + timedelta(minutes=self.settings.access_token_expire_minutes),
                  "scope": "openid",
                  "admin": admin
            }
            return jwt.encode(payload, self.settings.secret_key, algorithm=self.settings.algorithm)
      
      def decode(self, token: str = Depends(oauth2_scheme)):
            try:
                  decoded = jwt.decode(token, self.setting.secret_key, algorithm=self.settings.algorithm)
            except jwt.ExpiredSignatureError:
                  raise ValueError("Token has expired")
            except jwt.InvalidTokenError:
                  raise ValueError("Invalid token")
            
            return decoded