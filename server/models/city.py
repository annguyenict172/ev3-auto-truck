from db import db
from base import TimestampMixin


class City(TimestampMixin, db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng
