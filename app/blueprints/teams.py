from flask import Blueprint, render_template
from app.forms import TeamForm
from app.extensions import db
import pandas as pd

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('/teams')
def index():
    form = TeamForm()
    return render_template('teams/index.html', form=form)

@teams_bp.route('/teams/create', methods=['GET', 'POST'])
def create():
    form = TeamForm()
    # perform sql #
    # render html template with data #
    sql_general = f"select * from teams where teamname='{form.TeamName.data}'"
    df = pd.read_sql_query(sql_general, db.get_engine())
    general_rows = [row for index, row in df.iterrows()]

    sql_stats = f"select * from teamstats where teamid=(select teamid from teams where teamname='{form.TeamName.data}')"

    df_stats = pd.read_sql_query(sql_stats, db.get_engine())
    stat_rows = [row for index, row in df_stats.iterrows()]

    return render_template('teams/index.html',  
                    TeamName=form.TeamName.data,
                    general_rows=general_rows,
                    stat_rows=stat_rows,
                    tables=True, form=form)