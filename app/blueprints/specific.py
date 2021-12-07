from flask import Blueprint, render_template
import pandas as pd
from app.forms import SpecificForm
from app.extensions import db

specific_bp = Blueprint('specific', __name__)

@specific_bp.route('/specific')
def index():
    form = SpecificForm()

    return render_template('specific/index.html', form=form)

@specific_bp.route('/specific/create', methods=['GET', 'POST'])
def create():
    form = SpecificForm()

    age = form.Age.data

    sql_pts = f"""
    select ps.player, ps.pts from playerstats as ps join players as p on ps.player = p.name
    where ps.pts = (select max(ps.pts) from players as p join playerstats as ps on p.name=ps.player
    where age = {age})
    and p.age = {age};
    """

    sql_ast = f"""
    select ps.player, ps.ast from playerstats as ps join players as p on ps.player = p.name
    where ps.ast = (select max(ps.ast) from players as p join playerstats as ps on p.name=ps.player
    where age = {age})
    and p.age = {age};
    """

    sql_rbs = f"""
    select ps.player, ps.trb from playerstats as ps join players as p on ps.player = p.name
    where ps.trb = (select max(ps.trb) from players as p join playerstats as ps on p.name=ps.player
    where age = {age})
    and p.age = {age}; 
    """

    df_pts = pd.read_sql_query(sql_pts, db.get_engine())
    pts_rows = [row for index, row in df_pts.iterrows()]

    df_ast = pd.read_sql_query(sql_ast, db.get_engine())
    ast_rows = [row for index, row in df_ast.iterrows()]

    df_rbs = pd.read_sql_query(sql_rbs, db.get_engine())
    rbs_rows = [row for index, row in df_rbs.iterrows()]

    return render_template('specific/index.html', form=form, tables=True, age=age, pts_rows=pts_rows, ast_rows=ast_rows, rbs_rows=rbs_rows)
    