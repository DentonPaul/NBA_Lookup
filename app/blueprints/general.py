from flask import Blueprint, render_template
import pandas as pd
from app.extensions import db

general_bp = Blueprint('general', __name__)

@general_bp.route('/general')
def index():

    # join, group by, aggregate
    sql_age = """
    select age, avg(pts) as avg_points from players as p 
    join playerstats as ps on p.name=ps.player 
    group by age 
    order by age;
    """
    
    # join, group by, aggregate
    sql_pos = """
    select pos, avg(pts) as avg_points from players as p 
    join playerstats as ps on p.name=ps.player 
    group by pos;
    """

    # aggregate, subquery
    sql_max_pts = """
    select * from playerstats where pts = (select max(pts) from playerstats);
    """

    df_age = pd.read_sql_query(sql_age, db.get_engine())
    age_rows = [row for index, row in df_age.iterrows()]

    df_pos = pd.read_sql_query(sql_pos, db.get_engine())
    pos_rows = [row for index, row in df_pos.iterrows()]

    df_max_pts = pd.read_sql_query(sql_max_pts, db.get_engine())
    max_rows = [row for index, row in df_max_pts.iterrows()]

    return render_template('general/index.html', age_rows=age_rows, pos_rows=pos_rows, max_rows=max_rows)  