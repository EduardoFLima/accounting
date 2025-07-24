from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app(config_override=None):
    app = Flask(__name__)

    db_uri = str(os.environ.get("SQLALCHEMY_DATABASE_URI", 'postgresql://postgres:postgres@localhost:5432/accounting'))
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config_override:
        app.config.update(config_override)

    db.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app