from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.message_service import MessageService
from service.user_service import UserService

"""Message Controller handles all message related http requests.
"""
class MessageController(Resource):

    def __init__(self) -> None:
        self.message_service = MessageService()
        self.user_service = UserService()
    
    """GET method for all incoming message related http GET requests.
    Params: mthod - the selected operation, message_id - the id of a message.
    """
    @jwt_required()
    def get(self, method=None, message_id=None):
        user = self.user_service.get_user_by_id(get_jwt_identity())
        print(user.username)
        if not user:
            return {'message': 'User not found'}, 404
        if(method == 'getAll'):
            messages = {'messages': [msg.json() for msg in self.message_service.get_all_messages(user.username)]}
            print(messages)
            if not messages:
                return {'messages': 'No messages'}, 404
            return messages, 200
            
        if(method == 'getUnread'):
            unread_messages = self.message_service.get_all_unread_messages(user.username)
            print(unread_messages)
            if not unread_messages:
                return {'message': 'No unread messages'}, 404
            return {'Unread messages': [x.json() for x in unread_messages]}, 200

        if(method == 'getSingle'):
            message = self.message_service.read_single_message(user.username, message_id)
            if message:
                return {'message': message.json()}, 200
            return {'message': 'Message not found'}, 404

    
    """POST method for all incoming message related http POST requests.
    """
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('receiver',
            type=str,
            required=True,
            help="This field cannot be blank!"
            )
        parser.add_argument('message',
            type=str,
            required=True,
            help="This field cannot be blank!"
            )
        parser.add_argument('subject',
            type=str,
            required=True,
            help="This field cannot be blank!"
            )
        data = parser.parse_args()
        user = self.user_service.get_user_by_id(get_jwt_identity())
        if self.message_service.send_message(data, user.username):
            return {'message': 'The message was successfully sent to {0}'.format(data['receiver'])}, 201
        return {'message': 'Something went wrong, faild to send message.'}, 500

    """DELETE method for all incoming message related http DELETE requests.
    """
    @jwt_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message_id',
            type=int,
            required=True,
            help="This field cannot be blank!"
            )
        data = parser.parse_args()
        message_deleted = self.message_service.delete_message(data['message_id'], get_jwt_identity())
        if message_deleted:
            return {'message': 'Message Successfully deleted.'}, 200
        else:
            return {'message': 'Message not found.'}, 404
