import pusher
from flask import jsonify, request, Blueprint

position_bp = Blueprint('position_bp', __name__)

pusher_client = pusher.Pusher(
  app_id='524891',
  key='bc48ffab0f0d29ebe910',
  secret='4ccbafa61f0ddd0abf08',
  cluster='ap1',
  ssl=True
)


@position_bp.route('/locations', methods=['POST'])
def new_location():
    location_id = request.json.get('location_id')
    pusher_client.trigger('ans-team-887', 'change-position', {'location_id': location_id})
    return jsonify({})

