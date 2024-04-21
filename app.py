from flask import Flask
from utils.database import dBConnection
from routes.orderRoutes import order_bp


app=Flask(__name__)

dBConnection()

app.register_blueprint(order_bp)
