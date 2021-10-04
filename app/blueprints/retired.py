from flask import Blueprint, render_template

retired_bp = Blueprint('retired', __name__)

@retired_bp.route('/retired')
def index():
    return render_template('retired/index.html')