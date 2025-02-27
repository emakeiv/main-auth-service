from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from env_configuration import get_settings


try:
    settings = get_settings()

    DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine(settings.db_uri))
except Exception as e:
    print(f"Error initializing database connection: {e}")
    raise
