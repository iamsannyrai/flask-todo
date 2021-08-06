from datetime import datetime
from extensions import db


class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime)


class TodoModel(BaseModel):
    __tablename__ = 'todos'
    title = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.title
