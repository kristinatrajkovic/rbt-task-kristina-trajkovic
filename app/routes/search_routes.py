# from flask import Blueprint, request, jsonify
# from app.models.building import Building
# from app.models.property_meta import EstateType
# from app.models.location import CityPart
# from app.extensions import db
#
# search_bp = Blueprint('search', __name__)
#
# @search_bp.route('/properties/search', methods=['GET'])
# def search_properties():
#     query = Building.query
#
#     # filteri iz url parametara
#     property_type = request.args.get('property_type')  # "Stan" ili "Kuća"
#     min_sqft = request.args.get('min_square_footage', type=float)
#     max_sqft = request.args.get('max_square_footage', type=float)
#     parking = request.args.get('parking')  # "true" ili "false"
#     state = request.args.get('state')
#     estate_type = request.args.get('estate_type')
#
#     # primena filtera
#     if property_type:
#         query = query.join(Building.estate_type).filter(EstateType.name.ilike(f"%{property_type}%"))
#     if estate_type:
#         query = query.join(Building.estate_type).filter(EstateType.name.ilike(f"%{estate_type}%"))
#     if min_sqft is not None:
#         query = query.filter(Building.square_footage >= min_sqft)
#     if max_sqft is not None:
#         query = query.filter(Building.square_footage <= max_sqft)
#     if parking is not None:
#         query = query.filter(Building.parking == (parking.lower() == 'true'))
#     if state:
#         query = query.join(Building.city_part).join(CityPart.city).join(CityPart.city.state).filter(CityPart.city.state.name.ilike(f"%{state}%"))
#
#     # paginacija
#     page = request.args.get('page', 1, type=int)
#     per_page = request.args.get('per_page', 10, type=int)
#     paginated = query.paginate(page=page, per_page=per_page, error_out=False)
#
#     results = []
#     for prop in paginated.items:
#         results.append({
#             "id": prop.id,
#             "square_footage": prop.square_footage,
#             "price": prop.price,
#             "rooms": prop.rooms,
#             "bathrooms": prop.bathrooms,
#             "parking": prop.parking,
#             "estate_type": prop.estate_type.name if prop.estate_type else None,
#             "offer": prop.offer.name if prop.offer else None,
#             "city_part": prop.city_part.name if prop.city_part else None,
#         })
#
#     return jsonify({
#         "page": page,
#         "per_page": per_page,
#         "total": paginated.total,
#         "properties": results
#     })
#
