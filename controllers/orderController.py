from flask import jsonify
from model.orders import Order
from datetime import datetime, timezone
from utils.database import dBConnection
from utils.coordinates import getCoordinates

client, db, collection = dBConnection()

def placeOrder(data):
    try:
        cityLatitude, cityLongitude, countryLatitude, countryLongitude = getCoordinates(data['customerCity'], data['customerCountry'])
        newOrder = Order(
            data['price'], data['currency'], data['productCategories'],
            data['salesType'], data['phoneNumber'], data['quantity'], data['orderName'],
            data['customerCity'], data['customerCountry'],
            cityLatitude, cityLongitude, countryLatitude, countryLongitude,
            datetime.now(timezone.utc)
        )

        print("The newOrder is as:", newOrder.to_dict())

        order_Id = collection.insert_one(newOrder.to_dict()).inserted_id

        print("The order ID is as:", order_Id)
        orderId = str(order_Id)
        jsonData = jsonify({ "message": "Order placed Successfully", "order_id": orderId, "status": 'SUCCESSFUL'})
        return jsonData

    except Exception as e:
        print(f"An error occurred in controller while placing the order: {e}")
        return jsonify({"error": "Failed to place order"}), 500  
