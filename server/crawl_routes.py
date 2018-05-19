import json
import httplib2
import sys
import codecs

from models.route import Route
from models.place import Place

from db import db
from app import app

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)


def crawl_routes():
    google_api_key = "AIzaSyAOAM3a30FLWqmNg14u--MSIhteaboU2uQ"
    places = Place.query.all()
    for i in range(0, len(places)):
        for j in range(0, len(places)):
            if i == j:
                continue
            else:
                origin = places[i]
                destination = places[j]
                route = Route.query.filter_by(origin_id=origin.id, dest_id=destination.id).first()
                if route is not None:
                    continue
                url = ('https://maps.googleapis.com/maps/api/directions/json?origin={},{}&destination={},{}&key={}'.
                       format(origin.lat, origin.lng, destination.lat, destination.lng, google_api_key))
                h = httplib2.Http()
                result = json.loads(h.request(url, 'GET')[1])
                if len(result['routes']) != 0:
                    route = Route(
                        origin_id=origin.id,
                        dest_id=destination.id,
                        distance=result['routes'][0]['legs'][0]['distance']['value'],
                        time=result['routes'][0]['legs'][0]['duration']['value'],
                        route=result['routes'][0]['overview_polyline']['points'],
                    )
                else:
                    route = Route(
                        origin_id=origin.id,
                        dest_id=destination.id,
                        distance=-1,
                        time=-1,
                        route='-1'
                    )
                db.session.add(route)
                print(route.id)
                db.session.commit()


with app.app_context():
    db.init_app(app)
    db.create_all()
    crawl_routes()
