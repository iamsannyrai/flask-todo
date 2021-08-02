import json

from flask import request
from flask_restful import Resource, abort

from todo_app.schemas.todo_schema import TodoSchema
from todo_app.todo_manager import get_todo_list, create_todo, get_todo, delete_todo, update_todo

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


def abort_if_todo_doesnt_exist(todo_id):
    todo = get_todo(todo_id)
    if todo:
        todos = get_todo_list()
        if todo not in todos:
            abort(404, message="Todo with {} doesn't exist.".format(todo_id))
    else:
        abort(404, message="Todo with {} doesn't exist.".format(todo_id))


class TodoResource(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo = get_todo(todo_id)
        return todo_schema.dump(todo)

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        delete_todo(todo_id)
        return '', 204

    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo_dict = json.loads(request.data)
        todo = update_todo(todo_id, todo_dict)
        return todo_schema.dump(todo), 201


class TodoListResource(Resource):
    def get(self):
        todos = get_todo_list()
        return todos_schema.dump(todos)

    def post(self):
        todo_dict = json.loads(request.data)
        new_todo = create_todo(todo_dict)
        return todo_schema.dump(new_todo)
