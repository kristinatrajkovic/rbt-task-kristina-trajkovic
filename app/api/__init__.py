from flask import Blueprint
from app.api.properties.routes import properties_bp
from app.api.search.routes import search_bp

app = Blueprint('main', __name__)
app.register_blueprint(properties_bp)
app.register_blueprint(search_bp)
