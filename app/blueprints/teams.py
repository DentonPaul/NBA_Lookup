from flask import Blueprint, render_template

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('/teams')
def index():
    return render_template('teams/index.html')