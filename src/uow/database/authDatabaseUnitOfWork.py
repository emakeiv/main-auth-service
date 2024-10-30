
from src.uow.database.abstractDatabaseUnitOfWork import AbstractDatabaseUnitOfWork
from dal.repos.user_repo import UserRepository
from src.dal.db import factorySettings as database_factory


class DatabaseUnitOfWork(AbstractDatabaseUnitOfWork):

      def __init__(self, session_factory = database_factory.DEFAULT_SESSION_FACTORY):
            self.session_factory = session_factory

      def __enter__(self):
            self.session = self.session_factory()
            self.repos = UserRepository(self.session)
            return super().__enter__()
      
      def __exit__(self, *args):
            super().__exit__(*args)
            self.session.close()

      def commit(self):
            self.session.commit()

      def rollback(self):
            self.session.rollback()