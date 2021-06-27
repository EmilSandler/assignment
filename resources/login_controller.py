
from flask_restful import Resource, reqparse, request
from service.login_service import LoginService
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
    )


class LoginController(Resource):
    # The request parser makes sure the needed arguments sent in the request.
    # If an argument is missing, returns a message to the user (the 'help' field). 
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank!"
        )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank!"
        )

    
    def __init__(self):
        self.login_service = LoginService()



    """POST methos for all login related post requests.
    If the login is succeed, responce with JWT access token and refresh token.
    """
    
    def post(self):
        data = self.parser.parse_args()
        jwt_token = self.login_service.user_login(data)
        if jwt_token:
            return {
                'access_token': jwt_token['access_token'],
                'refresh_token': jwt_token['refresh_token']
            }, 200
        
        return {'message': 'Invalid credentials'}, 401



"""Refresh a JWT
with the refresh token given to the usr when login to the system.
"""
class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        curren_user = get_jwt_identity()
        new_token = create_access_token(identity=curren_user, fresh=False)
        return {'access_token': new_token}, 200