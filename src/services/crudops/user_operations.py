
from typing import List, Optional

from pydantic import (
    SecretStr,
    EmailStr
)

from dal.models.user import User
from uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork
from src.services.exceptions import DuplicateEmailError

from sqlalchemy.exc import IntegrityError, NoResultFound
from services.crypto_utils import (
      hash_password
)

class UserService:
      
      def __init__(self, uow: DatabaseUnitOfWork):
            self.uow = uow
      
      def create_user(self, username: str, email: EmailStr, password: SecretStr) -> User:
            
            hashed_password = hash_password(password.get_secret_value())
            new_user = User(
                  username=username, 
                  email=email, 
                  hashed_password=hashed_password)
            
            with self.uow as uow:
                  try:       
                        uow.repos.add(new_user)
                        uow.commit()
                        return new_user.dict()
                  except IntegrityError as e:
                        uow.rollback()
                        raise DuplicateEmailError("A user with this email already exists") from e

        

      def get_user(self, user_id:int) -> Optional[User]:
            with self.uow as uow:
                  try:
                        user = uow.repos.get(user_id)
                  except NoResultFound:
                        raise NoResultFound(f"User with ID {user_id} not found")
              
            return user
     
      def list_users(self) -> List[User]:
            with self.uow as uow:
                  users = uow.repos.list()
            return users

      def update_user(self):
            pass

      def delete_user(self, user_id:int) -> None:
            with self.uow as uow:
                  user = uow.repos.get(user_id)
                  if not user:
                        raise NoResultFound(f"User with ID {user_id} not found.")
                  uow.repos.delete(user_id)
                  uow.commit()