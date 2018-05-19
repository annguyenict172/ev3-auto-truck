from db import db
from base import TimestampMixin

from models.place import Place


class Route(TimestampMixin, db.Model):
    __tablename__ = 'route'
    id = db.Column(db.Integer, primary_key=True)
    origin_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    dest_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    distance = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    route = db.Column(db.String(200), nullable=False)

    origin = db.relationship('Place', foreign_keys=[origin_id])
    destination = db.relationship('Place', foreign_keys=[dest_id])

    def __init__(self, origin_id, dest_id, distance, time, route):
        self.origin_id = origin_id
        self.dest_id = dest_id
        self.distance = distance
        self.time = time
        self.route = route

    @property
    def serialize(self):
        return {
            'id': self.id,
            'origin': Place.query.filter_by(id=self.origin_id).first().serialize,
            'dest': Place.query.filter_by(id=self.dest_id).first().serialize,
            'time': self.time,
            'distance': self.distance,
            'route': self.route
        }
