from flask import Blueprint, jsonify, request
from models.place import Place
from models.route import Route
from engines.tsp import find_ideal_route, find_extreme_route

place_bp = Blueprint('place_bp', __name__)


@place_bp.route('/places', methods=['GET'])
def get_all_places():
    filters = []
    city_id = request.args.get('city_id')
    type_id = request.args.get('type_id')

    if city_id is not None:
        filters.append(Place.city_id == city_id)
    if type_id is not None:
        filters.append(Place.type_id == type_id)
    places = Place.query.filter(*filters).limit(29)
    return jsonify({"places": [p.serialize for p in places]})


@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.filter_by(id=place_id).first()
    return jsonify({
            'id': place.id,
            'name': place.name,
            'image_url': place.image_url,
            'location': {
                'lat': place.lat,
                'lng': place.lng
            },
            'rating': place.rating,
            'short_description': place.short_description,
            'long_description': place.long_description,
            'city_id': place.city_id,
            'type_id': place.type_id
        })


@place_bp.route('/routes', methods=['GET'])
def get_all_routes():
    weather_condition = request.args.get('weather_condition')
    place_ids = request.args.get('place_ids').split(',')
    if weather_condition == 0:
        results = find_ideal_route(place_ids, place_ids[0], place_ids[0])
    else:
        results = find_extreme_route(place_ids, place_ids[0])
    routes = []
    for i in range(0, len(results)):
        if i == len(results) - 1:
            routes.append(Route.query.filter_by(origin_id=results[i], dest_id=results[0]).first())
        else:
            routes.append(Route.query.filter_by(origin_id=results[i], dest_id=results[i+1]).first())
    print(len(routes))

    return jsonify({"routes": [r.serialize for r in routes]})

