from flask import jsonify
from model.orders import Order
from datetime import datetime, timezone
from utils.database import dBConnection

# Get MongoDB objects from the database module
client, db, collection = dBConnection()
print("The collection in controller:", collection)

def placeOrder(data):
    try:
        # Create the Order object
        newOrder = Order(data['price'], data['currency'], data['product_categories'],
                         data['sales_type'], data['quantity'], data['product_name'],
                         data['city'], data['country'], data['phone_number'],
                         datetime.now(timezone.utc))

        # Print information for debugging
        print("The newOrder is as:", newOrder.to_dict())

        # Insert order into collection
        order_Id = collection.insert_one(newOrder.to_dict()).inserted_id

        # Print confirmation and return order ID
        print("The order ID is as:", order_Id)
        orderId=str(order_Id)
        return jsonify({"status":"SUCCESSFUL", "orderId":orderId})

    except Exception as e:
        print(f"An error occurred while placing the order: {e}")
        return jsonify({"error": "Failed to place order"}), 500  
