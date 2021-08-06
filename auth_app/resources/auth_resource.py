import json

from flask import request
from flask_restful import Resource

from auth_app.auth_manager import create_user
from auth_app.schemas.user_schema import UserSchema

user_schema = UserSchema(exclude=['password'])


class RegistrationResource(Resource):
    def post(self):
        user_dict = json.loads(request.data)
        new_user = create_user(user_dict)
        return user_schema.dump(new_user)


class LoginResource(Resource):
    def post(self):
        pass
