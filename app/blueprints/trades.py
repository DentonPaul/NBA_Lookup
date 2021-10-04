from flask import Blueprint, render_template

trades_bp = Blueprint('trades', __name__)

@trades_bp.route('/trades')
def index():
    return render_template('trades/index.html')