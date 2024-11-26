from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'login'

    # Register blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

    return app
