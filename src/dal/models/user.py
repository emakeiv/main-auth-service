from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
      user_id: int
      username: str
      email: str
      password: str
      created_at: datetime
      edited_at: datetime


      def dict(self):
            return {
                  "id": self.user_id,
                  "name": self.username,
                  "email": self.email,
                  "password": self.password,
                  "created_at": self.created_at,
                  "edited_at": self.edited_at
            }