from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar("T")

class AbstractRepository(ABC, Generic[T]):

    @abstractmethod
    def get(self, entity_id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def add(self, entity: T) -> T:
        raise NotImplementedError
    
    @abstractmethod
    def list(self) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    def update(self, entiry_id: int, entity: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def delete(self, entiry_id: int) -> None:
        raise NotImplementedError