from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .routes import main


# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config['SECRET_KEY'] = '60ca969c3b2d0a7ec863dd5fdcd3c64e'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    from routes import main
    from admin_routes import admin
    from user_routes import user
    
    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(user)

    # Create database models
    with app.app_context():
        db.create_all()

    return app
