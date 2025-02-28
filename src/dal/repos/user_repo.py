from typing import List, Any, Optional
from sqlalchemy.orm.exc import NoResultFound

from dal.models.user import User
from dal.repos.abstract_repo import AbstractRepository


class UserRepository(AbstractRepository):

    def __init__(self, session) -> None:
        self.session = session

    def add(self, user):
        try:
            # print(f"will try to add this {user} to the database")
            self.session.add(user)
        except Exception as e:
            print(e)
            raise e

    def get(self, reference: Any) -> Optional[User]:
        return self.session.query(User).filter((User.username == reference) | (User.email == reference)).one()

    def list(self) -> List[User]:
        return self.session.query(User).all()

    def update(self, user_id: int, user: User):
        pass

    def delete(self, user_id: int) -> None:
        user = self.get(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
