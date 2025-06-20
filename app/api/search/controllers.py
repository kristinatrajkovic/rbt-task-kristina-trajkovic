from flask import jsonify
from app.models.building import Building
from app.models.property_meta import EstateType
from app.models.location import CityPart

def search_properties(args):
    query = Building.query

    def get_arg(key, cast=str):
        val = args.get(key)
        return cast(val) if val else None

    filters = {
        'property_type': get_arg("property_type"),
        'estate_type': get_arg("estate_type"),
        'min_sqft': get_arg("min_square_footage", float),
        'max_sqft': get_arg("max_square_footage", float),
        'parking': get_arg("parking", lambda v: v.lower() == 'true'),
        'state': get_arg("state")
    }

    if filters['property_type']:
        query = query.join(Building.estate_type).filter(EstateType.name.ilike(f"%{filters['property_type']}%"))
    if filters['estate_type']:
        query = query.join(Building.estate_type).filter(EstateType.name.ilike(f"%{filters['estate_type']}%"))
    if filters['min_sqft']:
        query = query.filter(Building.square_footage >= filters['min_sqft'])
    if filters['max_sqft']:
        query = query.filter(Building.square_footage <= filters['max_sqft'])
    if filters['parking'] is not None:
        query = query.filter(Building.parking == filters['parking'])
    if filters['state']:
        query = query.join(Building.city_part).join(CityPart.city).join(CityPart.city.state).filter(CityPart.city.state.name.ilike(f"%{filters['state']}%"))

    page = get_arg("page", int) or 1
    per_page = get_arg("per_page", int) or 10
    paginated = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "page": page,
        "per_page": per_page,
        "total": paginated.total,
        "properties": [_serialize_property(p) for p in paginated.items]
    })

def _serialize_property(prop):
    return {
        "id": prop.id,
        "square_footage": prop.square_footage,
        "price": prop.price,
        "rooms": prop.rooms,
        "bathrooms": prop.bathrooms,
        "parking": prop.parking,
        "estate_type": prop.estate_type.name if prop.estate_type else None,
        "offer": prop.offer.name if prop.offer else None,
        "city_part": prop.city_part.name if prop.city_part else None,
    }
