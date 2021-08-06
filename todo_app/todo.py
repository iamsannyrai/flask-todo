from flask import Blueprint
from flask_restful import Api

from todo_app.resources.todo_resource import TodoListResource, TodoResource

todo_app = Blueprint('todo_app', __name__)
api = Api(todo_app)

api.add_resource(TodoListResource, '')
api.add_resource(TodoResource, '/<todo_id>')
