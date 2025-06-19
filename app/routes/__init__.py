from flask import Blueprint
from .property_routes import properties_bp
from .search_routes import search_bp


main = Blueprint('main', __name__)
main.register_blueprint(properties_bp)
main.register_blueprint(search_bp)

