from flask_cors import CORS

from app import app
from db import db

db.init_app(app)
CORS(app)


@app.before_first_request
def create_tables():
    db.create_all()
