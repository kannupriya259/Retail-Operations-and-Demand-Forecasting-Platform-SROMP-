from flask import Blueprint, request, jsonify
from utils import execute_query

sales_blueprint = Blueprint('sales', __name__)

@sales_blueprint.route("/", methods=["GET"])
def get_sales():
    query = "SELECT * FROM sales"
    result = execute_query(query)
    return jsonify(result)

@sales_blueprint.route("/", methods=["POST"])
def add_sale():
    data = request.json
    query = "INSERT INTO sales (product_id, quantity_sold) VALUES (%s, %s)"
    execute_query(query, (data['product_id'], data['quantity_sold']))
    return jsonify({"message": "Sale recorded successfully"}), 201
