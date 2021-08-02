from datetime import datetime
from extensions import db

from todo_app.models.todo_model import TodoModel


def create_todo(todo):
    todo = TodoModel(title=todo['title'], description=todo['description'])
    db.session.add(todo)
    db.session.commit()
    return todo


def get_todo(todo_id):
    return TodoModel.query.get(todo_id)


def update_todo(todo_id, todo):
    existing_todo = get_todo(todo_id)
    existing_todo.title = todo['title'],
    existing_todo.description = todo['description'],
    existing_todo.updated_at = datetime.utcnow()
    db.session.commit()
    return existing_todo


def delete_todo(todo_id):
    todo = get_todo(todo_id)
    db.session.delete(todo)
    db.session.commit()


def get_todo_list():
    return TodoModel.query.all()
