from flask import Flask
from .extensions import db, migrate
# from .routes import main
from .models import *
# from .extensions import db, migrate, jwt

# from app.api.properties import properties_bp
# app.register_blueprint(properties_bp)

from app.api.properties.routes import properties_bp
from app.api.search.routes import search_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # app.register_blueprint(main)
    app.register_blueprint(properties_bp)
    app.register_blueprint(search_bp)

    # jwt.init_app(app)

    return app




