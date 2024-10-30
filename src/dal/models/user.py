from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    username: str
    email: str
    password: str
    user_id: Optional[int] = field(default=None)
    created_at: Optional[datetime] = field(default=None)
    edited_at: Optional[datetime] = field(default=None)

    def dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
            "edited_at": self.edited_at
        }
