from datetime import datetime
from extensions import db


class BaseModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime())


class TodoModel(BaseModel):
    title = db.Column(db.String())
    description = db.Column(db.String())

    def __repr__(self):
        return '<Todo %r>' % self.title
