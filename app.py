import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.registartion_controller import RegistrationController
from resources.login_controller import LoginController, TokenRefresh
from resources.message_controller import MessageController



# Load the environment variable.


# An object of Flask class, Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# Set Database URI from the .env file
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']

#If set to True (the default) Flask-SQLAlchemy will track modifications of objects and emit signals.
#  This requires extra memory and can be disabled if not needed.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enable flask-JWT error messages
app.config['PROPOGATE_EXCEPTIONS'] = True

#JWT secret key value from the .env file
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']


api = Api(app)



jwt = JWTManager(app)

# Add resources to the api (set up controllers and endpoints)
api.add_resource(RegistrationController, '/register')
api.add_resource(LoginController, '/login')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(MessageController, '/message/send', '/message/delete', '/message/<string:method>',  '/message/<string:method>/<int:message_id>')

if __name__ == '__main__':
    app.run()