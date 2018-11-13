from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from cinemax.config import Configuration


app = Flask(__name__, template_folder='front/templates',
    static_folder='front/static')
app.config.from_object(Configuration)
db = SQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
