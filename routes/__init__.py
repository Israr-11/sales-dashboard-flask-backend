from flask import Blueprint

# Initialize a Blueprint for task routes
task_bp = Blueprint('task_bp', __name__)

# Import routes from task_routes module
from . import task_routes
