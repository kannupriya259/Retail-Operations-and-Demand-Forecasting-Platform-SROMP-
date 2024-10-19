from flask import Blueprint, request, jsonify
from utils import execute_query

inventory_blueprint = Blueprint('inventory', __name__)

@inventory_blueprint.route("/", methods=["GET"])
def get_inventory():
    query = "SELECT * FROM inventory"
    result = execute_query(query)
    return jsonify(result)

@inventory_blueprint.route("/", methods=["POST"])
def add_item():
    data = request.json
    query = "INSERT INTO inventory (product_name, quantity, reorder_level) VALUES (%s, %s, %s)"
    execute_query(query, (data['product_name'], data['quantity'], data['reorder_level']))
    return jsonify({"message": "Item added successfully"}), 201
