from db import db
from base import TimestampMixin


class Type(TimestampMixin, db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    def __init__(self, name):
        self.name = name
