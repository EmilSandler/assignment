from operator import sub
from db import db
import datetime

"""The message class represents a Message entity.
"""
class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80))
    receiver = db.Column(db.String(80))
    message = db.Column(db.String(255))
    subject = db.Column(db.String(80))
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now())
    message_unread = db.Column(db.Boolean)
    
    def __init__(self, sender, receiver, message, subject, creation_date, message_unread):
       self.sender = sender
       self.receiver = receiver
       self.message = message
       self.subject = subject
       self.creation_date = creation_date
       self.message_unread = message_unread

    def json(self):
        return {
            'sender': self.sender,
            'receiver':self.receiver,
            'message':self.message,
            'subject':self.subject,
            'creation_date':str(self.creation_date),
            'message_unread':self.message_unread
        }