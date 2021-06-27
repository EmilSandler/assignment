
from repository.user_repository import UserRepository
from db import db
from entity.user import User;
from sqlalchemy import exc

"""User Registration Service.
Handles the registration proccess.
"""
class UserRegistrationService:
    
    def __init__(self) -> None:
        self.user_repository = UserRepository()
        
    """Register a new Application User.

    If user exists return False, else creates a new User 
    and saves him in the Database and return True.
    """
    
    def register_user(self, username, password):
        try:
            user_exists = self.user_repository.find_by_username(username)
        except exc.SQLAlchemyError as e:
                print(e)
                return False
        if user_exists:
            return False
        new_user = User(username, password)
        try:
            self.user_repository.save_to_db(new_user)
        except exc.SQLAlchemyError as e:
                    print(e)
                    return False
        return True
