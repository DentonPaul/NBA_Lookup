from flask import Blueprint, render_template
from app.forms import PlayerLookupForm, PlayerAddForm
import pandas as pd
from app.extensions import db
from sqlalchemy import func
from app.models import Player_Stats

players_bp = Blueprint('players', __name__)

@players_bp.route('/players')
def index():
    form = PlayerLookupForm()
    return render_template('players/index.html', form=form)

@players_bp.route('/players/search', methods=['GET', 'POST'])
def search():
    form = PlayerLookupForm()

    # player simple stats
    sql_general = f"select pos, age from players where name='{form.PlayerName.data}'"
    df = pd.read_sql_query(sql_general, db.get_engine())
    general_rows = [row for index, row in df.iterrows()]
    print(general_rows)

    # player stats
    sql_stats = f"select * from playerstats where player='{form.PlayerName.data}'"
    df_stats = pd.read_sql_query(sql_stats, db.get_engine())
    stat_rows = [row for index, row in df_stats.iterrows()]

    return render_template('players/index.html',  
                    PlayerName=form.PlayerName.data,
                    general_rows=general_rows,
                    stat_rows=stat_rows,
                    tables=True, form=form)

# @players_bp.route('/players/add')
# def add():
#     form = PlayerAddForm()
#     return render_template('players/add.html', form=form)

# @players_bp.route('/players/add/create', methods=['GET', 'POST'])
# def addcreate():
#     form = PlayerAddForm()

#     ## stats
#     fgp = round(form.fg.data / form.fga.data, 4)
#     threepp = round(form.threep.data / form.threepa.data, 4)
#     twopp = round(form.twop.data / form.twopa.data, 4)
#     ftp = round(form.ft.data / form.fta.data, 4)
#     trb = form.orb.data + form.drb.data

#     sql_team = f"select teamabbr from teams where teamname='{form.team.data}'"
    
#     df_team = pd.read_sql_query(sql_team, db.get_engine())

#     rows = [row for index, row in df_team.iterrows()]
#     tm = rows[0][0]

#     sql_stats = f"""
#     INSERT INTO playerstats(player, tm, gms, gstart, mp, fg, fga, fgp, threep, threepa, threepp, 
#     twop, twopa, twopp, efgp, ft, fta, ftp, orb, drb, trb, ast, stl, blk, tov, pf, pts)
#     VALUES ('{form.PlayerName.data}', '{tm}', {form.gms.data}, 0, 0, {form.fg.data},
#     {form.fga.data}, {fgp}, {form.threep.data}, {form.threepa.data}, {threepp}, {form.twop.data}, 
#     {form.twopa.data}, {twopp}, 0, {form.ft.data}, {form.fta.data}, {ftp}, {form.orb.data}, 
#     {form.drb.data}, {trb}, {form.ast.data}, {form.stl.data}, {form.blk.data}, {form.tov.data},
#     {form.pf.data}, {form.pts.data});
#     """

#     db.engine.execute(sql_stats)
#     db.session.commit()

#     stats = [[form.PlayerName.data], [form.team.data], [form.gms.data], [0], [0], [form.fg.data],
#     [form.fga.data], [fgp], [form.threep.data], [form.threepa.data], [threepp], [form.twop.data], 
#     [form.twopa.data], [twopp], [0], [form.ft.data], [form.fta.data], [ftp], [form.orb.data], 
#     [form.drb.data], [trb], [form.ast.data], [form.stl.data], [form.blk.data], [form.tov.data],
#     [form.pf.data], [form.pts.data]]

#     cols = ['player', 'tm', 'gms', 'gstart', 'mp', 'fg', 'fga', 'fgp', 'threep', 'threepa', 'threepp', 
#     'twop', 'twopa', 'twopp', 'efgp', 'ft', 'fta', 'ftp', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

#     d = pd.DataFrame(dict(zip(cols, stats)))

#     stat_rows = [row for index, row in d.iterrows()]


#     ## player
#     sql_general = f"""
#     INSERT INTO players(name, pos, age)
#     VALUES ('{form.PlayerName.data}', '{form.pos.data}', {form.age.data});
#     """

#     db.engine.execute(sql_general)
#     db.session.commit()


#     df_gen = pd.DataFrame(dict(name=[form.PlayerName.data], pos=[form.pos.data], age=[form.age.data]))
#     general_rows = [row for index, row in df_gen.iterrows()]

#     return render_template('players/search.html',  
#                     message=f"Successfully added {form.PlayerName.data}!",
#                     PlayerName=form.PlayerName.data,
#                     general_rows=general_rows,
#                     stat_rows=stat_rows,
#                     tables=True, form=form)