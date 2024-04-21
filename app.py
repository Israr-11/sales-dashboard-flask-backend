from flask import Flask
from routes.orderRoutes import order_bp

app=Flask(__name__)

app.register_blueprint(order_bp)
