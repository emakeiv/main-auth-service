from abc import ABC, abstractmethod


class AbstractDatabaseUnitOfWork(ABC):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError
