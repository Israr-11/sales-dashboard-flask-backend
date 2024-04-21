from flask import Blueprint, jsonify, request
from controllers.orderController import placeOrder

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/place_order', methods=['POST'])
def place_order():
    try:
        order_id = placeOrder(request.json)
        return jsonify(str(order_id))
    except Exception as e:
        print(f"An error occurred while placing the order: {e}")
        return jsonify({"error": "Failed to place order"}), 500
