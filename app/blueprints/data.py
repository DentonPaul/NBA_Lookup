from flask import Blueprint
import pandas as pd
from flask import render_template
from app.extensions import db

see_data_bp = Blueprint('test_raw_sql', __name__)

@see_data_bp.route('/data/<db_name>')
def coaches(db_name):

    dbs = ['coaches', 'coachstats', 'teams', 'teamstats', 'players', 'playerstats', 'topscorers']
    if db_name.lower() not in dbs:
        return f"database name must be one of these: {dbs}"
    df = pd.read_sql_query(f'select * from {db_name}', db.get_engine())
    return render_template('data/index.html',  title=db_name, tables=[df.to_html(classes='data', header="true")], titles=df.columns.values)





    return "success"





