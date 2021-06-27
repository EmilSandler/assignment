from entity.user import User
from flask_sqlalchemy import SQLAlchemy
from db import db


"""The User Repository is responsible for
fetching User data from the database.
"""
class UserRepository:

    def __init__(self):
        self.db = SQLAlchemy()
    
    # Find a user by his ID
    def find_by_id(self, _id):
        return User.query.filter_by(id=_id).first()

    # Find a user by his Username
    def find_by_username(self, username):
        return User.query.filter_by(username=username).first()

    # Save a user to the DB
    def save_to_db(self, user):
        self.db.session.add(user)
        self.db.session.commit()