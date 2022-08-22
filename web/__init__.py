from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)

    # Run the configurations to setup the URIs
    # before initializing the db and other variables
    app.config.from_object("config.Config")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        # Imports
        from . import serve

        # Initialize Global db
        db.drop_all()
        db.create_all()

        return app