from db import db


class Warehouse(db.Model):
    __tablename__ = 'warehouses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    lighting_condition = db.Column(db.String(40), nullable=False)
    location_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, temperature, lighting_condition, location_id):
        self.name = name
        self.temperature = temperature
        self.lighting_condition = lighting_condition
        self.location_id = location_id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'temperature': self.temperature,
            'lighting_condition': self.lighting_condition,
            'location_id': self.location_id
        }

