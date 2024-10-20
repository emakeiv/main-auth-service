from datetime import datetime
from sqlalchemy.orm import registry
from sqlalchemy.schema import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime

from dal.models.user import User

metadata = MetaData()
mapper_registry = registry(metadata=metadata)
users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
    Column('email', String(255), nullable=False, unique=True),
    Column('password', String(255), nullable=False),
    Column('created_at', DateTime, default=datetime.now(datetime.UTC)),
    Column('edited_at', DateTime, default=datetime.now(datetime.UTC), onupdate=datetime.now(datetime.UTC))
)
                  

def start_mappers():
    mapper_registry.map_imperatively(User, users_table)