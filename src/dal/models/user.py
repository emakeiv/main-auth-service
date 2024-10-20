from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
      id: int
      name: str
      email: str
      password: str
      created_at: datetime
      edited_at: datetime


      def dict(self):
            return {
                  "id": self.id,
                  "name": self.name,
                  "email": self.email,
                  "password": self.password,
                  "created_at": self.created_at,
                  "edited_at": self.edited_at
            }