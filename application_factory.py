from flask import Flask

from extensions import db, ma
from todo_app.todo import todo_app


def create_app(config_file):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_file)
    flask_app.register_blueprint(todo_app, url_prefix="/api")
    db.init_app(flask_app)
    ma.init_app(flask_app)
    return flask_app
