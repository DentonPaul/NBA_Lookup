from re import L, T
from flask import Blueprint
import pandas as pd
import numpy as np
from app.extensions import db
from app.models import Coach_Stats, Teams, Coaches, Player_Stats, Players, Team_Stats, Top_Scorers

test_raw_sql_bp = Blueprint('test_raw_sql', __name__)

@test_raw_sql_bp.route('/test')
def index():

    result = db.engine.execute('select * from teams')
    names = [row[0] for row in result]

    return str(names)



