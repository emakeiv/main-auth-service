
from typing import List, Optional
from dal.models.user import User
from uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork
from src.services.exceptions import DuplicateEmailError

from sqlalchemy.exc import IntegrityError, NoResultFound

class UserService:

      def __init__(self, uow: DatabaseUnitOfWork):
            self.uow = uow
      def create_user(self, username: str, email: str, password: str) -> User:
            new_user = User(
                  username=username, 
                  email=email, 
                  password=password)
            
            with self.uow as uow:
                  try:  
                        # print(f"user: {new_user.dict()}")
                        uow.repos.add(new_user)
                        uow.commit()
                        return new_user.dict()
                  except IntegrityError as e:
                        uow.rollback()
                        # print(f'the error: {e}')
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