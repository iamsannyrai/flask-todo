from auth_app.models.user_model import UserModel
from extensions import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
