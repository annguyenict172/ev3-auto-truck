from app import app
from db import db
import models
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def _make_context():
    return dict(app=app, db=db, models=models)


manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
