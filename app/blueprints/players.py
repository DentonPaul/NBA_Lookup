from flask import Blueprint, render_template
from app.forms import PlayerLookupForm
import pandas as pd
from app.extensions import db
from sqlalchemy import func

players_bp = Blueprint('players', __name__)

@players_bp.route('/players')
def index():
    form = PlayerLookupForm()
    return render_template('players/index.html', form=form)

@players_bp.route('/players/search', methods=['GET', 'POST'])
def search():
    form = PlayerLookupForm()

    #####
    # Raw SQL
    sql_general = f"select pos, age from players USE INDEX (player_index) where name='{form.PlayerName.data}'"
    df = pd.read_sql_query(sql_general, db.get_engine())
    #####

    if df.shape[0] == 0:
        message_2 = f"{form.PlayerName.data} is not in our database. Please Try Again."
        return render_template('players/index.html', form=form, message_2=message_2)
    general_rows = [row for index, row in df.iterrows()]

    #####
    # Raw SQL, INDEX
    sql_stats = f"""
    select * from playerstats USE INDEX (playerstats_index)
    where player = '{form.PlayerName.data}'
    """
    df_stats = pd.read_sql_query(sql_stats, db.get_engine())
    #####

    stat_rows = [row for index, row in df_stats.iterrows()]

    return render_template('players/index.html',  
                    PlayerName=form.PlayerName.data,
                    general_rows=general_rows,
                    stat_rows=stat_rows,
                    tables=True, form=form)