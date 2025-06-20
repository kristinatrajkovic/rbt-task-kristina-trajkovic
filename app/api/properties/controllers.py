from flask import jsonify, abort
from app.models.building import Building
from app.extensions import db

def get_property(property_id):
    prop = Building.query.get(property_id)
    if not prop:
        abort(404, description="Property not found")
    return jsonify(_serialize_property(prop))

def create_property(data):
    required_fields = ['square_footage', 'rooms', 'bathrooms', 'price', 'parking', 'registration', 'estate_type_id', 'offer_id', 'city_part_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    new_property = Building(**{field: data[field] for field in required_fields})
    new_property.construction_year = data.get('construction_year')
    new_property.land_area = data.get('land_area')

    db.session.add(new_property)
    db.session.commit()

    return jsonify({"message": "Property created", "id": new_property.id}), 201

def update_property(property_id, data):
    prop = Building.query.get(property_id)
    if not prop:
        return jsonify({"error": "Property not found"}), 404

    for field in ['square_footage', 'rooms', 'bathrooms', 'price', 'parking', 'registration', 'construction_year', 'land_area', 'estate_type_id', 'offer_id', 'city_part_id']:
        if field in data:
            setattr(prop, field, data[field])

    db.session.commit()
    return jsonify({"message": "Property updated", "id": prop.id}), 200

def _serialize_property(prop):
    return {
        "id": prop.id,
        "square_footage": prop.square_footage,
        "land_area": prop.land_area,
        "rooms": prop.rooms,
        "bathrooms": prop.bathrooms,
        "price": prop.price,
        "parking": prop.parking,
        "registration": prop.registration,
        "construction_year": prop.construction_year,
        "estate_type": prop.estate_type.name if prop.estate_type else None,
        "offer": prop.offer.name if prop.offer else None,
        "city_part": prop.city_part.name if prop.city_part else None,
    }
