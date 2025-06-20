from flask import Blueprint, request
from .controllers import search_properties

search_bp = Blueprint('search', __name__)

@search_bp.route('/properties/search', methods=['GET'])
def search():
    return search_properties(request.args)
