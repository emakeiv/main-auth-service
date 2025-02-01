
import jwt
import bcrypt
from  datetime import datetime, timedelta

from dal.models.user import User
from env_configuration import get_settings
from uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork

class AuthService():
      def __init__(self, uow: DatabaseUnitOfWork):
                self.uow = uow
                self.settings = get_settings() 
        
      def hash_password(self, password: str) -> str:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            return hashed_password.decode('utf-8')

      def match_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
      
      def authenticate_user(self, reference: str, password:str) -> User:
            with self.uow as uow:      
                  user = uow.repos.get(reference) 
                  if not user:
                        raise ValueError("Invalid email or password")                       
                  if not self.match_password(password, user.password):
                        raise ValueError("Invalid email or password")                        
                  return user

      def encode(self, user:User, admin:bool):
            now = datetime.now(tz=datetime.timezone.utc)
            payload = {
                  "sub": user.email,
                  "user_id": user.user_id,
                  "exp": now + timedelta(minutes=self.settings.access_token_expire_minutes),
                  "iat": now,
                  "admin": admin
            }
            return jwt.encode(payload, self.settings.secret_key, algorithm=self.settings.algorithm)
      
      def decode(self, encoded_data):
            try:
                  decoded = jwt.decode(encoded_data, self.setting.secret_key, algorithm=self.settings.algorithm)
            except jwt.ExpiredSignatureError:
                  raise ValueError("Token has expired")
            except jwt.InvalidTokenError:
                  raise ValueError("Invalid token")
            
            return decoded