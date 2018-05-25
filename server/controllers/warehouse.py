from flask import Blueprint, jsonify, request
import pusher
from db import db

from models.warehouse import Warehouse


pusher_client = pusher.Pusher(
  app_id='524891',
  key='bc48ffab0f0d29ebe910',
  secret='4ccbafa61f0ddd0abf08',
  cluster='ap1',
  ssl=True
)

warehouse_bp = Blueprint('warehouse_bp', __name__)


@warehouse_bp.route('/warehouses', methods=['GET'])
def get_all_warehouses():
    warehouses = Warehouse.query.all()
    return jsonify({"warehouses": [w.serialize for w in warehouses]})


@warehouse_bp.route('/warehouses', methods=['PUT'])
def update_warehouse():
    first_warehouse_temp = request.json.get('temp_1')
    second_warehouse_temp = request.json.get('temp_2')
    first_warehouse_humid = request.json.get('humi_1')
    second_warehouse_humid = request.json.get('humi_2')
    warehouse_num = request.json.get('warehouse_num')

    first_warehouse = Warehouse.query.filter_by(id=1).first()
    first_warehouse.temperature = first_warehouse_temp
    first_warehouse.lighting_condition = first_warehouse_humid

    second_warehouse = Warehouse.query.filter_by(id=2).first()
    second_warehouse.temperature = second_warehouse_temp
    second_warehouse.lighting_condition = second_warehouse_humid

    db.session.commit()

    pusher_client.trigger('ans-team-887', 'choose-warehouse', {'warehouse_num': warehouse_num})

    return jsonify({})


@warehouse_bp.route('/robots', methods=['PUT'])
def update_robot_status():
    status = request.json.get('status')
    pusher_client.trigger('ans-team-887', 'change-status', {'status': status})
    return jsonify({})


@warehouse_bp.route('/locations', methods=['POST'])
def new_location():
    location_id = request.json.get('location_id')
    pusher_client.trigger('ans-team-887', 'change-position', {'location_id': location_id})
    return jsonify({})
