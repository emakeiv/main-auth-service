from fastapi.security import HTTPBearer

from src.uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork


def get_uow():
    return DatabaseUnitOfWork()


def get_security_schema() -> HTTPBearer:
    return HTTPBearer()
