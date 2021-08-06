import json

from flask import request
from flask_restful import Resource

from auth_app.auth_manager import create_user, find_user_by_email, generate_access_token, generate_refresh_token
from auth_app.schemas.user_schema import UserSchema
from extensions import bcrypt

user_schema = UserSchema(exclude=['password'])


def encrypt_password(password: str):
    encrypted = bcrypt.generate_password_hash(password).decode('utf-8')
    return encrypted


def check_if_password_matches(encrypted, plain):
    return bcrypt.check_password_hash(encrypted, plain)


class RegistrationResource(Resource):
    def post(self):
        user_dict = json.loads(request.data)
        encrypted_password = encrypt_password(user_dict['password'])
        user_dict['password'] = encrypted_password
        new_user = create_user(user_dict)
        return user_schema.dump(new_user)


class LoginResource(Resource):
    def post(self):
        credential = json.loads(request.data)
        user = find_user_by_email(credential['email'])
        if not user:
            return {'message': 'No user found'}
        else:
            is_valid = check_if_password_matches(user.password, credential['password'])
            if is_valid:
                access_token = generate_access_token(user.id)
                refresh_token = generate_refresh_token(user.id)
                return {'email': user.email, 'message': 'Login Successful', 'access_token': access_token,
                        'refresh_token': refresh_token}
            else:
                return {'message': 'Password do not match'}
