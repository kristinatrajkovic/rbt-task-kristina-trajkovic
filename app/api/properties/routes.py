from flask import Blueprint, request
from .controllers import get_property, create_property, update_property
from app.utils.decorators import token_required

properties_bp = Blueprint('properties', __name__)

@properties_bp.route('/properties/<int:property_id>', methods=['GET'])
def get_property_route(property_id):
    return get_property(property_id)

@properties_bp.route('/properties', methods=['POST'])
@token_required
def create_property_route():
    return create_property(request.get_json())

@properties_bp.route('/properties/<int:property_id>', methods=['PUT'])
@token_required
def update_property_route(property_id):
    return update_property(property_id, request.get_json())
