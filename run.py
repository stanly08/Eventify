from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .routes import main
    app.register_blueprint(main)

    # Register other blueprints if needed

    return app
