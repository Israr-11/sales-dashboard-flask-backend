import json
from flask import jsonify
from model.orders import Order
from datetime import datetime, timezone
from utils.database import dBConnection

client, db, collection = dBConnection()

def placeOrder(data):
    try:
        newOrder = Order(data['price'], data['currency'], data['product_categories'],
                         data['sales_type'], data['quantity'], data['product_name'],
                         data['city'], data['country'], data['phone_number'],
                         datetime.now(timezone.utc))

        print("The newOrder is as:", newOrder.to_dict())

        order_Id = collection.insert_one(newOrder.to_dict()).inserted_id

        print("The order ID is as:", order_Id)
        orderId = str(order_Id)
        jsonData = jsonify({ "message":"Order placed Sucessfully", "status":'SUCCESSFUL', "order_id":orderId})
        return jsonData

    except Exception as e:
        print(f"An error occurred while placing the order: {e}")
        return jsonify({"error": "Failed to place order"}), 500  
