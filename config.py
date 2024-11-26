import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///events.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'app/static/uploads'

    @staticmethod
    def init_app(app):
        """Initializes the application with additional configurations."""
        # Add any initialization here
        print("Database URI from config:", app.config['SQLALCHEMY_DATABASE_URI'])  # Debugging statement

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    
    # Continue with your Flask app setup
    # For example, initialize SQLAlchemy and other extensions here
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)
    
    print("App configuration:", app.config)  # Debugging statement
