from flask import Blueprint, jsonify, request
from models.warehouse import Warehouse

warehouse_bp = Blueprint('warehouse_bp', __name__)


@warehouse_bp.route('/warehouses', methods=['GET'])
def get_all_warehouses():
    warehouses = Warehouse.query.all()
    return jsonify({"warehouses": [w.serialize for w in warehouses]})
