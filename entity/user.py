from db import db

"""The User class represents a User entity.
"""
class User(db.Model): 

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self,username, password):
        self.username = username
        self.password = password
    
    def json(self):
        return{
            'id': self.id,
            'username': self.username
        }