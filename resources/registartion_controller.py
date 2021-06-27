
from flask_restful import Resource, reqparse
from service.registration_service import UserRegistrationService
from werkzeug.security import generate_password_hash



class RegistrationController(Resource):
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

    def __init__(self) -> None:
        self.registration_service = UserRegistrationService()


    """POST method for all incoming registration related http POST requests.
    """
    def post(self):
        data = RegistrationController.parser.parse_args()
        if not self.registration_service.register_user(data['username'],generate_password_hash(data['password'])):
            return {"message": "A user with that username already exists"}, 400
            
        return {"message": "User created successfully"}, 201