from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

# for encrypting and decrypting password
bcrypt = Bcrypt()

jwt = JWTManager()
