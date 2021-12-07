from flask import Blueprint, render_template
import pandas as pd
from app.extensions import db

initialize_bp = Blueprint('initialize', __name__)

@initialize_bp.route('/initialize')
def index():
    # Stored Procedure
    sql = "CALL GetPlayer('LeBron James');"
    df = pd.read_sql_query(sql, db.get_engine())

    return df.to_html()