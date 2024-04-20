from flask import Flask
from utils.database import databaseConnection
from routes.order_routes import order_bp


app=Flask(__name__)

databaseConnection()

app.register_blueprint(order_bp)
