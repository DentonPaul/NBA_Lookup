from re import L, T
from flask import Blueprint
import pandas as pd
import numpy as np
from app.extensions import db
from app.models import Coach_Stats, Teams, Coaches, Player_Stats, Players, Team_Stats, Top_Scorers

from sqlalchemy import text

reset_data_bp = Blueprint('reset_data', __name__)

@reset_data_bp.route('/reset_data')
def index():

    # delete data from tables

    db.session.query(Coach_Stats).delete()
    db.session.commit()
    db.session.query(Teams).delete()
    db.session.commit()
    db.session.query(Coaches).delete()
    db.session.commit()
    db.session.query(Player_Stats).delete()
    db.session.commit()
    db.session.query(Players).delete()
    db.session.commit()
    db.session.query(Team_Stats).delete()
    db.session.commit()
    db.session.query(Top_Scorers).delete()
    db.session.commit()

    # add data
    df = pd.read_csv('app/static/files/Teams.csv')
    df = df.replace(np.nan, -1)

    for index, row in df.iterrows():
        team = Teams(teamid=row.TeamID, teamname=row.TeamName, teamabbr=row.TeamAbbr, location=row.Location)
        db.session.add(team)
        db.session.commit()

    df = pd.read_csv('app/static/files/Coach_Stats.csv')
    df = df.replace(np.nan, -1)
    for index, row in df.iterrows():
        coach_stat = Coach_Stats(
            name=row.Name,
            team=row.Team,
            seasg=row.SeasG,
            seasw=row.SeasW,
            seasl=row.SeasL,
            frang=row.FranG,
            franw=row.FranW,
            franl=row.FranL,
            carew=row.CareW,
            carel=row.CareL,
            carewp=row.CareWP,
            poseasg=row.POSeasG,
            poseasw=row.POSeasW,
            poseasl=row.POSeasL,
            pofrang=row.POFranG,
            pofranw=row.POFranW,
            pofranl=row.POFranL,
            pocareg=row.POCareG,
            pocarew=row.POCareW,
            pocarel=row.POCareL
        )
        db.session.add(coach_stat)
        db.session.commit()

    df = pd.read_csv('app/static/files/Coaches.csv')

    for index, row in df.iterrows():
        coach = Coaches(name=row.Name, teamid=row.TeamID)
        db.session.add(coach)
        db.session.commit()

    df = pd.read_csv('app/static/files/Player_Stats.csv')
    df = df.replace(np.nan, -1)
    for index, row in df.iterrows():
        player_stats = Player_Stats(
            player=row.Player,
            tm = row.Tm,
            gms = row.Gms,
            gstart = row.Gstart,
            mp = row.MP,
            fg = row.FG,
            fga = row.FGA,
            fgp = row.FGP,
            threep = row.ThreeP,
            threepa = row.ThreePA,
            threepp = row.ThreePP,
            twop = row.TwoP,
            twopa = row.TwoPA,
            twopp = row.TwoPP,
            efgp = row.eFGP,
            ft = row.FT,
            fta = row.FTA,
            ftp = row.FTP,
            orb = row.ORB,
            drb = row.DRB,
            trb = row.TRB,
            ast = row.AST,
            stl = row.STL,
            blk = row.BLK,
            tov = row.TOV,
            pf = row.PF,
            pts = row.PTS
        )

        db.session.add(player_stats)
        db.session.commit()

    df = pd.read_csv('app/static/files/Players.csv')
    
    for index, row in df.iterrows():
        player = Players(name=row.Name, pos=row.Pos, age=row.Age)
        db.session.add(player)
        db.session.commit()

    df = pd.read_csv('app/static/files/Team_Stats.csv')
    
    for index, row in df.iterrows():
        team_stats = Team_Stats(
            teamid=row.TeamID,
            gms=row.Gms,
            mp=row.MP,
            fg=row.FG,
            fga=row.FGA,
            fgp=row.FGP,
            threep=row.ThreeP,
            threepa=row.ThreePA,
            threepp=row.ThreePP,
            twop=row.TwoP,
            twopa=row.TwoPA,
            twopp=row.TwoPP,
            ft=row.FT,
            fta=row.FTA,
            ftp=row.FTP,
            orb=row.ORB,
            drb=row.DRB,
            trb=row.TRB,
            ast=row.AST,
            stl=row.STL,
            blk=row.BLK,
            tov=row.TOV,
            pf=row.PF,
            pts=row.PTS
        )
        db.session.add(team_stats)
        db.session.commit()

    df = pd.read_csv('app/static/files/Top_Scorers.csv')
    df = df.replace(np.nan, -1)
    for index, row in df.iterrows():
        top_scorer = Top_Scorers(
            points=row.Points,
            name=row.Name,
            year=row.Year,
            teamname=row.TeamName,
            oppteamname=row.OppTeamName,
            teamscore=row.TeamScore,
            oppteamscore=row.OppTeamScore,
            minsplayed=row.MinsPlayed
        )

        db.session.add(top_scorer)
        db.session.commit()

    db.engine.execute('select * from teams')

    return "Success! All data has been reset."