from flask import Blueprint, render_template
from app.forms import CoachLookupForm
import pandas as pd
from app.extensions import db
from sqlalchemy import func

coaches_bp = Blueprint('coaches', __name__)

@coaches_bp.route('/coaches')
def index():
    form = CoachLookupForm()
    return render_template('coaches/index.html', form=form)

@coaches_bp.route('/coaches/search', methods=['GET', 'POST'])
def search():
    form = CoachLookupForm()

    #####
    # Raw SQL, INDEX
    sql_stats = f"""
    select teams.teamname, cs.seasg, cs.seasw, 
    cs.seasl, cs.frang, cs.franw, cs.franl, 
    cs.carew, cs.carel, cs.carewp, cs.poseasg, 
    cs.poseasw, cs.poseasl, cs.pofrang, cs.pofranw,
    cs.pofranl, cs.pocareg, cs.pocarew, cs.pocarel
    from coachstats as cs USE INDEX (coachstats_index) 
    join coaches as c on cs.name=c.name join teams on c.teamid=teams.teamid
    where cs.name = '{form.CoachName.data}';
    """
    df = pd.read_sql_query(sql_stats, db.get_engine())
    #####

    stat_rows = [row for index, row in df.iterrows()]

    return render_template('coaches/index.html', CoachName=form.CoachName.data, 
                stat_rows=stat_rows, tables=True, form=form)