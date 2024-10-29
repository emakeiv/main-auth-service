from pydantic import BaseModel, EmailStr, StringConstraints , Field
from typing_extensions import Annotated
from datetime import datetime
from typing import List

UsernameConstrainedStr = Annotated[str, StringConstraints(min_length=1, max_length=255)]
PasswordConstrainedStr = Annotated[str, StringConstraints(min_length=6)]

class UserSchema(BaseModel):
    username: UsernameConstrainedStr
    email: EmailStr
    password: PasswordConstrainedStr
  


class UsersListSchema(BaseModel):
    users: List[UserSchema]

class UserResponseSchema(BaseModel):
    user_id: int
    username: str
    email: str
    created_at: datetime