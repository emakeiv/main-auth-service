from pydantic import (
    BaseModel, 
    EmailStr, 
    SecretStr,
    Field
)

from typing_extensions import Annotated
from datetime import datetime
from typing import List

UsernameConstrainedStr = Annotated[str, Field(..., min_length=1, max_length=255)]
PasswordConstrainedStr = Annotated[str, Field(..., min_length=8)]

class UserSchema(BaseModel):
    username: UsernameConstrainedStr
    email: EmailStr = Field(...)
    password: SecretStr
  

class UsersListSchema(BaseModel):
    users: List[UserSchema]

class UserResponseSchema(BaseModel):
    user_id: int
    username: str
    email: str
    created_at: datetime
    edited_at: datetime
    
    class Config:
        from_attributes = True