from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import Config
from werkzeug.debug import DebuggedApplication
db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        from app import routes, models, schemas
        db.create_all()
    return app

app = create_app()
