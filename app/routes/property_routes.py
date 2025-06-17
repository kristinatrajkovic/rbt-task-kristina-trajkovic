from flask import Blueprint, jsonify, request, abort
from app.models import Building
from app.extensions import db

properties_bp = Blueprint('properties', __name__)

@properties_bp.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = Building.query.get(property_id)
    if not property:
        abort(404, description="Property not found")
    return jsonify({
        "id": property.id,
        "square_footage": property.square_footage,
        "land_area": property.land_area,
        "rooms": property.rooms,
        "bathrooms": property.bathrooms,
        "price": property.price,
        "parking": property.parking,
        "registration": property.registration,
        "construction_year": property.construction_year,
        "estate_type": property.estate_type.name if property.estate_type else None,
        "offer": property.offer.name if property.offer else None,
        "city_part": property.city_part.name if property.city_part else None
    })

@properties_bp.route('/properties', methods=['POST'])
def create_property():
    data = request.get_json()

    required_fields = ['square_footage', 'rooms', 'bathrooms', 'price', 'parking', 'registration', 'estate_type_id', 'offer_id', 'city_part_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    new_property = Building(
        square_footage = data['square_footage'],
        rooms = data['rooms'],
        bathrooms = data['bathrooms'],
        price = data['price'],
        parking = data['parking'],
        registration = data['registration'],
        construction_year = data.get('construction_year'),
        land_area = data.get('land_area'),
        estate_type_id = data['estate_type_id'],
        offer_id = data['offer_id'],
        city_part_id = data['city_part_id']
    )

    db.session.add(new_property)
    db.session.commit()

    return jsonify({"message": "Property created", "id": new_property.id}), 201

@properties_bp.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    property = Building.query.get(property_id)
    if not property:
        return jsonify({"error": "Property not found"}), 404

    data = request.get_json()

    property.square_footage = data.get('square_footage', property.square_footage)
    property.rooms = data.get('rooms', property.rooms)
    property.bathrooms = data.get('bathrooms', property.bathrooms)
    property.price = data.get('price', property.price)
    property.parking = data.get('parking', property.parking)
    property.registration = data.get('registration', property.registration)
    property.construction_year = data.get('construction_year', property.construction_year)
    property.land_area = data.get('land_area', property.land_area)
    property.estate_type_id = data.get('estate_type_id', property.estate_type_id)
    property.offer_id = data.get('offer_id', property.offer_id)
    property.city_part_id = data.get('city_part_id', property.city_part_id)

    db.session.commit()

    return jsonify({"message": "Property updated", "id": property.id}), 200

