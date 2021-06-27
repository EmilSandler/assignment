from repository.user_repository import UserRepository
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import check_password_hash
from sqlalchemy import exc

"""Login Service.
Handles the Login proccess.
"""
class LoginService:
    
    def __init__(self):
        self.user_repository = UserRepository()
        
    """User Login.
    If the user exists and the give password matches to the existing user password,
    create access token and refresh token and return them as a dict.
    Else return False.
    """
    
    def user_login(self, data):
        try:
            user = self.user_repository.find_by_username(data['username'])
        except exc.SQLAlchemyError as e:
                print(e)
                return False
        if user and LoginService.verify_password(data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        return False

    """Verifying the given password with the password saved in the Database."""
    @classmethod
    def verify_password(cls, password_input, password_db):
        return check_password_hash(password_db, password_input)