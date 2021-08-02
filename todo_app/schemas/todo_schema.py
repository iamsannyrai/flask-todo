from extensions import ma
from todo_app.models.todo_model import TodoModel


class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TodoModel
