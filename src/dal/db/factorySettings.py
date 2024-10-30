from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuration import settings

DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine(settings.db_uri))
