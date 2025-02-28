from dal.models.user import User
from services.crypto.common_utils import match_password
from uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork

from src.services.security.token_utils import decode, encode


class AuthService:
    def __init__(self, uow: DatabaseUnitOfWork):
        self.uow = uow

    def authenticate_user(self, reference: str, password: str) -> User:
        with self.uow as uow:
            user = uow.repos.get(reference)
           
            if not user:
                raise ValueError("Invalid email or password")
            if not match_password(password.get_secret_value(), user.hashed_password):
                raise ValueError("Invalid email or password")
            return user.dict()

    def generate_token(self, user: dict):
        return encode(user["user_id"])

    def verify_token(self, token):
        return decode(token)
