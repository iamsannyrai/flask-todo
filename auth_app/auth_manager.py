from auth_app.models.user_model import UserModel
from extensions import db


def create_user(user):
    new_user = UserModel(first_name=user['first_name'], last_name=user['last_name'], email=user['email'],
                         password=user['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user
