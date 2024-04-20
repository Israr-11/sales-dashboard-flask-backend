from flask import Blueprint

# Initialize a Blueprint for task routes
order_bp = Blueprint('order_bp', __name__)

# Import routes from task_routes module
from . import order_bp
