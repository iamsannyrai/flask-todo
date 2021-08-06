from uuid import uuid4

from extensions import db
from todo_app.models.todo_model import TodoModel


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    first_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    todos = db.relationship(TodoModel, backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % (self.first_name + self.last_name)
