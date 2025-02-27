from src.uow.database.authDatabaseUnitOfWork import DatabaseUnitOfWork


def get_uow():
    return DatabaseUnitOfWork()
