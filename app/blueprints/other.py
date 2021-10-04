from flask import Blueprint, render_template

other_bp = Blueprint('other', __name__)

@other_bp.route('/other')
def index():
    return render_template('other/index.html')