from flask import Blueprint, render_template

drafted_bp = Blueprint('drafted', __name__)

@drafted_bp.route('/drafted')
def index():
    return render_template('drafted/index.html')