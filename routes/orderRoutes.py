from flask import Blueprint, jsonify, request
from controllers.orderController import placeOrder

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/place_order', methods=['POST'])
def placeOrderRoute():
    try:
        orderId = placeOrder(request.json)
        return orderId
    except Exception as e:
        print(f"An error occurred in routes while placing the order: {e}")
        return jsonify({"error": "Failed to place order"}), 500