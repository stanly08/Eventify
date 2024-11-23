from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
print("Database URI: ", app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
