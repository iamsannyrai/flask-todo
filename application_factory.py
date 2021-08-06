from flask import Flask

from auth_app.auth import auth_app
from todo_app.todo import todo_app

from extensions import db, ma, migrate, bcrypt, jwt


def create_app(config_file):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_file)
    flask_app.register_blueprint(auth_app, url_prefix='/api/auth')
    flask_app.register_blueprint(todo_app, url_prefix="/api/todos")
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)
    ma.init_app(flask_app)
    bcrypt.init_app(flask_app)
    jwt.init_app(flask_app)
    return flask_app
