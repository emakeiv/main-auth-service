from sqlalchemy import create_engine
from sqlalchemy.orm import session_maker
from configuration import settings

DEFAULT_SESSION_FACTORY = session_maker(bind=create_engine(settings.db_uri))
