from flask import Blueprint, render_template
from app.forms import PlayerAddForm
import pandas as pd
from app.extensions import db

drafted_bp = Blueprint('drafted', __name__)

@drafted_bp.route('/drafted')
def index():
    form = PlayerAddForm()
    return render_template('drafted/index.html', form=form)

@drafted_bp.route('/drafted/create', methods=['GET', 'POST'])
def add():
    form = PlayerAddForm()

    ## stats
    fgp = round(form.fg.data / form.fga.data, 4)
    threepp = round(form.threep.data / form.threepa.data, 4)
    twopp = round(form.twop.data / form.twopa.data, 4)
    ftp = round(form.ft.data / form.fta.data, 4)
    trb = form.orb.data + form.drb.data

    #####
    # Raw SQL
    sql_team = f"select teamabbr from teams where teamname='{form.team.data}'"
    df_team = pd.read_sql_query(sql_team, db.get_engine())
    #####

    rows = [row for index, row in df_team.iterrows()]
    tm = rows[0][0]

    #####
    # Raw SQL
    sql_stats = f"""
    INSERT INTO playerstats(player, tm, gms, gstart, mp, fg, fga, fgp, threep, threepa, threepp, 
    twop, twopa, twopp, efgp, ft, fta, ftp, orb, drb, trb, ast, stl, blk, tov, pf, pts)
    VALUES ('{form.PlayerName.data}', '{tm}', {form.gms.data}, 0, 0, {form.fg.data},
    {form.fga.data}, {fgp}, {form.threep.data}, {form.threepa.data}, {threepp}, {form.twop.data}, 
    {form.twopa.data}, {twopp}, 0, {form.ft.data}, {form.fta.data}, {ftp}, {form.orb.data}, 
    {form.drb.data}, {trb}, {form.ast.data}, {form.stl.data}, {form.blk.data}, {form.tov.data},
    {form.pf.data}, {form.pts.data});
    """
    db.engine.execute(sql_stats)
    db.session.commit()
    #####


    stats = [[form.PlayerName.data], [form.team.data], [form.gms.data], [0], [0], [form.fg.data],
    [form.fga.data], [fgp], [form.threep.data], [form.threepa.data], [threepp], [form.twop.data], 
    [form.twopa.data], [twopp], [0], [form.ft.data], [form.fta.data], [ftp], [form.orb.data], 
    [form.drb.data], [trb], [form.ast.data], [form.stl.data], [form.blk.data], [form.tov.data],
    [form.pf.data], [form.pts.data]]

    cols = ['player', 'tm', 'gms', 'gstart', 'mp', 'fg', 'fga', 'fgp', 'threep', 'threepa', 'threepp', 
    'twop', 'twopa', 'twopp', 'efgp', 'ft', 'fta', 'ftp', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

    d = pd.DataFrame(dict(zip(cols, stats)))

    stat_rows = [row for index, row in d.iterrows()]


    #####
    # Raw SQL
    sql_general = f"""
    INSERT INTO players(name, pos, age)
    VALUES ('{form.PlayerName.data}', '{form.pos.data}', {form.age.data});
    """
    db.engine.execute(sql_general)
    db.session.commit()
    #####

    df_gen = pd.DataFrame(dict(name=[form.PlayerName.data], pos=[form.pos.data], age=[form.age.data]))
    general_rows = [row for index, row in df_gen.iterrows()]

    return render_template('players/index.html',  
                    message=f"Successfully added {form.PlayerName.data}!",
                    PlayerName=form.PlayerName.data,
                    general_rows=general_rows,
                    stat_rows=stat_rows,
                    tables=True, form=form)