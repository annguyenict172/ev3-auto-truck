from flask_cors import CORS

from app import app
from db import db

CORS(app)
db.init_app(app)

if __name__ == "__main__":
    app.run()
