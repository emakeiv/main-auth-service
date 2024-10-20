from dal.models.user import User
from abstract_repo import AbstractRepository


class UserRepository(AbstractRepository):

      def __init__(self, session) -> None:
            self.session = session

      def add(self, user):
            try:
                  self.session.add(user)
            except Exception as e:
                  print(e)
                  raise e
      
      def get(self, user_id: int):
            return self.session.query(User).filter_by(reference=user_id).one()
      def list(self):
            pass
      
      def update(self):
            pass

      def delete(selfs):
            pass