from flask import Blueprint, render_template

# Create a blueprint for routes
bp = Blueprint('main', __name__)

# Define route and view function
@bp.route('/')
def index():
    return render_template('index.html')

# Define another route and view function
@bp.route('/about')
def about():
    return render_template('about.html')
