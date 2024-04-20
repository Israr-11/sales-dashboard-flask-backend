from flask import Flask,jsonify
from model.orders import Order
from datetime import datetime, timezone
from utils.database import databaseConnection

db, collection_name, client=databaseConnection()
print("The collection is as in controller:", collection_name)

def placeOrder(data):
    try:
        # Create the Order object
        newOrder = Order(data['price'], data['currency'], data['product_categories'],
                         data['sales_type'], data['quantity'], data['product_name'],
                         data['city'], data['country'], data['phone_number'],
                         datetime.now(timezone.utc))

        # Print information for debugging
        print("The newOrder is as:", newOrder.to_dict())

        # Insert order into database
        order_id = collection_name.insert_one(newOrder.to_dict()).inserted_id

        # Print confirmation and return order ID
        print("The order ID is as:", order_id)
        return jsonify(str(order_id))

    except Exception as e:
        # Handle any exception that occurs during order creation or insertion
        print(f"An error occurred while placing the order: {e}")
        return jsonify({"error": "Failed to place order"}), 500  # Internal Server Error
