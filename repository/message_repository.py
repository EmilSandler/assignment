from entity.message import Message
from flask_sqlalchemy import SQLAlchemy


from db import db

"""The Message Repository is responsible for
fetching Message data from the database.
"""
class MessageRepository:

    def __init__(self):
        self.db = SQLAlchemy()
    
    # Save a message to the DB
    def save_to_db(self, message):
        self.db.session.add(message)
        self.db.session.commit()

    # Update an existing message in the DB
    def update_message(self, messages):
        for msg in messages:
            db.session.merge(msg)
            db.session.commit()

    # Delete a message from the DB
    def delete_from_db(self, message):
        db.session.delete(message)
        db.session.commit()


    # Find a message by message ID
    def find_by_id(self, _id):
        return Message.query.filter_by(id=_id).first()
    
    # Get all incoming messages
    def get_all(self, receiver):
        return Message.query.filter_by(receiver=receiver)