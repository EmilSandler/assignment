from repository.user_repository import UserRepository
from sqlalchemy import exc


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    """Get User by his ID and return the user.
    """
    def get_user_by_id(self, user_id):
        try:
            user = self.user_repository.find_by_id(user_id)
            return user
        except exc.SQLAlchemyError as e:
                print(e)
        return None
        