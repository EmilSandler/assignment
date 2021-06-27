from service.user_service import UserService
from entity.message import Message
from repository.message_repository import MessageRepository
from datetime import datetime
from sqlalchemy import exc

class MessageService:
    
    def __init__(self):
        self.message_repository = MessageRepository()
        self.user_service = UserService()


    """Send message to a specific user.

    If the message was sent return true, else return false,
    """
    def send_message(self, data, sender):
        new_message = Message(sender, data['receiver'], data['message'], data['subject'],datetime.now(), True)
        try:
            self.message_repository.save_to_db(new_message)
            return True 
        except exc.SQLAlchemyError as e:
                print(e)
                return False

    
    """Delete a message by message_id.

    A message can be deleted by the sender or the receiver,
    if the message is not found or the user not found return false.

    If the message is found and the user is the sender or the receiver,
    delete the message and return true/
    """
    def delete_message(self,message_id, user_id):
        message = self.message_repository.find_by_id(message_id)
        user = self.user_service.get_user_by_id(user_id)

        if not message or not user:
            return False
        
        if user.username == message.sender or user.username == message.receiver:
            try:
                self.message_repository.delete_from_db(message)
            except exc.SQLAlchemyError as e:
                print(e)
        return True

    """Get all messages of a specific user.
    Only the message receiver can get all his messages.

    If a message is unread, it wiil be mark as read.
    """
    def get_all_messages(self, username):
        try:
            user_messages = self.message_repository.get_all(username)
            
            for msg in user_messages:
                msg.message_unread = False 
            try:
                self.message_repository.update_message(user_messages)
            except exc.SQLAlchemyError as e:
                print(e)
                return False

            return user_messages
            
        except Exception as e:
            print(e)
            return False
        
        
    """Get all unread messages.
    All found messages will be mark as read.
    """
    def get_all_unread_messages(self, username):
        try:
            user_messages = self.message_repository.get_all(username)
            user_messages = list(filter(lambda x: x.message_unread and x.receiver == username , user_messages))
            if len(user_messages) > 0:
                for msg in user_messages:
                    msg.message_unread = False
                
                self.message_repository.update_message([msg])
                return user_messages
        except exc.SQLAlchemyError as e:
                print(e)
                return False

        return []

    """Get one single message by the message ID.
    """
    def read_single_message(self, user_id, message_id):
        try:
            message = self.message_repository.find_by_id(message_id)
        except exc.SQLAlchemyError as e:
                print(e)
                return False
        
        return message
       