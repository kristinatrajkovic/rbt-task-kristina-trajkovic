from flask import Flask
from .extensions import db, migrate
from .routes import main
from .models import *
# from .extensions import db, migrate, jwt


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    # jwt.init_app(app)

    return app




