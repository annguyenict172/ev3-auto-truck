from flask import Flask
from flask_cors import CORS

from controllers.warehouse import warehouse_bp
from models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super_secret_key'

app.register_blueprint(warehouse_bp)

cors = CORS(send_wildcard=True)
cors.init_app(app)


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        db.create_all()
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True)
