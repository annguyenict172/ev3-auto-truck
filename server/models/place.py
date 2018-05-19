from db import db
from base import TimestampMixin
from city import City
from type import Type


class Place(TimestampMixin, db.Model):
    __tablename__ = 'place'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float)
    image_url = db.Column(db.String(400))
    short_description = db.Column(db.String(400))
    long_description = db.Column(db.String(5000))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))

    city = db.relationship('City', foreign_keys=[city_id])
    type = db.relationship('Type', foreign_keys=[type_id])

    def __init__(self, _id, name, lat, lng, rating, image_url, short_description, long_description, city_id, type_id):
        self.id = _id
        self.name = name
        self.lat = lat
        self.lng = lng
        self.rating = rating
        self.image_url = image_url
        self.short_description = short_description
        self.long_description = long_description
        self.city_id = city_id
        self.type_id = type_id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url,
            'location': {
                'lat': self.lat,
                'lng': self.lng
            },
            'rating': self.rating,
            'short_description': self.short_description,
            'city_id': self.city_id,
            'type_id': self.type_id
        }
