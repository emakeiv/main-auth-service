from datetime import datetime, timezone
from sqlalchemy.orm import registry
from sqlalchemy.schema import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime

from dal.models.user import User

metadata = MetaData()
mapper_registry = registry(metadata=metadata)
users_table = Table('users', metadata,
    Column('user_id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), nullable=False),
    Column('email', String(255), nullable=False, unique=True),
    Column('hashed_password', String(255), nullable=False),
    Column('created_at', DateTime, default=datetime.now(timezone.utc)),
    Column('edited_at', DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
)
                  

def start_mappers():
    mapper_registry.map_imperatively(User, users_table)