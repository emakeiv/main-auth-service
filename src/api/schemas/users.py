from pydantic import BaseModel
from datetime import datatime

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datatime
    edited_at: datatime
