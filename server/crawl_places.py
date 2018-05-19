import json
import httplib2
import sys
import codecs

from models.place import Place
from db import db
from app import app

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

db.init_app(app)

next_page_token = 'CvQD6wEAALmLdoEu1zsIZMhROozjpqnByp57JetQQWbvaZcmE7xQDOKY7uWudpZPP3WH8Zc7izd6pFO8kXNjoK8rgZf93e28i7Xy9z2UG5nxujwuMUcQZJp2haV3mL9MW8e_Tr_VyvNQThUi8kdrXKxArKHv0-ixB10CePI7gforya7LGHE7On0uicZXvJUTGg2T8Woi3iY8CatS5T_5stSVmNoPei_zzEgLlUq5RK05cV_ugYBLqy2R8jm_5_hxq9s5IWmNG-sSfE7NDJjFUoEkIT4kNn5RsDhFnKUtpfy_7zzjXqoQlX4xqPkdHlOtJYAYi8-Uaw9Fz5PpMsr00_kVaWuykpjuKQIkQHfNH_e1scp35rA-Bf4w8kQO3I8Li1tzt6vMbWK4L-5NdP9XILka_ge2ALaV19QT_7nl2Gf1_lxvNmJmntXECYnC_rB4zmD5kxN9xH_9yxc3cboOXDEKjBmRiI9J1cqjOFDrtjkzzCB0KZ2GpnnfhCajfAk6qi9OA-oWPsABvICrmEw02mbmDvFKndaPSnCrvQBRe7I-_5RT6NUOu6sOSANeA7sc7J7uK28a9s3LYC_hA8AXOiex6xkfAH3BjvDhubgBQHSMFlL4_vsftNjp1tQExu8BY4Miv78crWgNqiJnleQaeCnUhCxyCgQSEAWfmHF30RWFzpTg-rv4LlIaFHJ71xKfPD7qljt9-fD7j0Soi-cR'


def crawl_places():
    global next_page_token
    google_api_key = "AIzaSyAOAM3a30FLWqmNg14u--MSIhteaboU2uQ"
    url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=amusement_park&location=35.6895,139.6917'
           '&radius=50000&key={}&pagetoken={}'.format(google_api_key, next_page_token))
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    print(result)
    next_page_token = result.get('next_page_token')
    places = result['results']
    for place in places:
        image_url = ''
        photo = place.get('photos')
        if photo is not None and photo[0] is not None:
            image_url = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}' \
                                     '&key={}'.format(place['photos'][0]['photo_reference'], google_api_key)
        new_place = Place(_id=place['id'],
                          name=place['name'],
                          lat=place['geometry']['location']['lat'],
                          lng=place['geometry']['location']['lng'],
                          rating=place.get('rating'),
                          image_url=image_url,
                          city_id=1
                          )
        try:
            db.session.add(new_place)
            db.session.commit()
        except:
            continue


with app.app_context():
    print(next_page_token)
    while next_page_token is not None:
        crawl_places()
