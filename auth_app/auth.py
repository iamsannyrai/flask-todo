from flask import Blueprint
from flask_restful import Api

from auth_app.resources.auth_resource import RegistrationResource, LoginResource

auth_app = Blueprint('auth_app', __name__)
api = Api(auth_app)

api.add_resource(RegistrationResource, '/register')
api.add_resource(LoginResource, '/login')
