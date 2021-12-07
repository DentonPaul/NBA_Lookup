from flask import Blueprint, render_template
from app.forms import TradeForm
from app.extensions import db
import pandas as pd
from app.models import Player_Stats

trades_bp = Blueprint('trades', __name__)

@trades_bp.route('/trades')
def index():
    form = TradeForm()
    return render_template('trades/index.html', form=form)

@trades_bp.route('/trades/create', methods=['GET', 'POST'])
def create():
    form = TradeForm()


    #####
    # Raw SQL
    sql_check_player = f"select * from players where name = '{form.PlayerName.data}'"
    df_check = pd.read_sql_query(sql_check_player, db.get_engine())
    #####

    if df_check.shape[0] == 0:
        message = f"{form.PlayerName.data} is not a valid player name. Try again."
        return render_template("trades/index.html", form=form, message=message)

    #####
    # Raw SQL
    sql_get_tm_abbrev = f"select teamabbr from teams where teamname = '{form.TeamName.data}'"
    df = pd.read_sql_query(sql_get_tm_abbrev, db.get_engine())
    #####

    team_abbr = df.teamabbr[0]

    #####
    # ORM
    db.session.query(Player_Stats)\
       .filter(Player_Stats.player == form.PlayerName.data)\
       .update({Player_Stats.tm: team_abbr})
    db.session.commit()
    #####

    message = f"Success! {form.PlayerName.data} is now on team: {form.TeamName.data} ({team_abbr})"
    return render_template("trades/index.html", form=form, message=message)