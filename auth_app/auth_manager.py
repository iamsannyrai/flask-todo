import datetime

from flask_jwt_extended import create_access_token, create_refresh_token

from auth_app.models.user_model import UserModel
from extensions import db


def generate_access_token(user):
    access_token = create_access_token(identity=user, expires_delta=datetime.timedelta(days=30))
    return access_token


def generate_refresh_token(user):
    refresh_token = create_refresh_token(identity=user)
    return refresh_token


def create_user(user):
    new_user = UserModel(first_name=user['first_name'], last_name=user['last_name'], email=user['email'],
                         password=user['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user


def find_user_by_email(email) -> UserModel:
    return UserModel.query.filter_by(email=email).first()
