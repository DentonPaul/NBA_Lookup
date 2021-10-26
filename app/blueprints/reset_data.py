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
    # db.session.execute()
    # sql = text('select * from Teams')
    return db.engine.table_names()
    # result = db.engine.execute(sql)
    # names = [row[0] for row in result]
    # print names
    # db.session.execute('Select * From Teams')
    # db.session.execute('DELETE from Teams;')
    # db.session.execute('DELETE from Coach_Stats;')
    # db.session.execute('DELETE from Coaches;')
    # db.session.execute('DELETE from Player_Stats;')
    # db.session.execute('DELETE from Players;')
    # db.session.execute('DELETE from Team_Stats;')
    # db.session.execute('DELETE from Top_Scorers;')

    # df = pd.read_csv('app/static/files/Teams.csv')
    # df = df.replace(np.nan, -1)

    # for index, row in df.iterrows():
    #     team = Teams(TeamID=row.TeamID, TeamName=row.TeamName, TeamAbbr=row.TeamAbbr, Location=row.Location)
    #     db.session.add(team)
    #     db.session.commit()

    # df = pd.read_csv('app/static/files/Coach_Stats.csv')
    # df = df.replace(np.nan, -1)
    # for index, row in df.iterrows():
    #     coach_stat = Coach_Stats(
    #         Name=row.Name,
    #         Team=row.Team,
    #         SeasG=row.SeasG,
    #         SeasW=row.SeasW,
    #         SeasL=row.SeasL,
    #         FranG=row.FranG,
    #         FranW=row.FranW,
    #         FranL=row.FranL,
    #         CareW=row.CareW,
    #         CareL=row.CareL,
    #         CareWP=row.CareWP,
    #         POSeasG=row.POSeasG,
    #         POSeasW=row.POSeasW,
    #         POSeasL=row.POSeasL,
    #         POFranG=row.POFranG,
    #         POFranW=row.POFranW,
    #         POFranL=row.POFranL,
    #         POCareG=row.POCareG,
    #         POCareW=row.POCareW,
    #         POCareL=row.POCareL
    #     )
    #     db.session.add(coach_stat)
    #     db.session.commit()

    # df = pd.read_csv('app/static/files/Coaches.csv')

    # for index, row in df.iterrows():
    #     coach = Coaches(Name=row.Name, TeamID=row.TeamID)
    #     db.session.add(coach)
    #     db.session.commit()

    # df = pd.read_csv('app/static/files/Player_Stats.csv')
    # df = df.replace(np.nan, -1)
    # for index, row in df.iterrows():
    #     player_stats = Player_Stats(
    #         Player=row.Player,
    #         Tm = row.Tm,
    #         Gms = row.Gms,
    #         Gstart = row.Gstart,
    #         MP = row.MP,
    #         FG = row.FG,
    #         FGA = row.FGA,
    #         FGP = row.FGP,
    #         ThreeP = row.ThreeP,
    #         ThreePA = row.ThreePA,
    #         ThreePP = row.ThreePP,
    #         TwoP = row.TwoP,
    #         TwoPA = row.TwoPA,
    #         TwoPP = row.TwoPP,
    #         eFGP = row.eFGP,
    #         FT = row.FT,
    #         FTA = row.FTA,
    #         FTP = row.FTP,
    #         ORB = row.ORB,
    #         DRB = row.DRB,
    #         TRB = row.TRB,
    #         AST = row.AST,
    #         STL = row.STL,
    #         BLK = row.BLK,
    #         TOV = row.TOV,
    #         PF = row.PF,
    #         PTS = row.PTS
    #     )

    #     db.session.add(player_stats)
    #     db.session.commit()

    # df = pd.read_csv('app/static/files/Players.csv')
    
    # for index, row in df.iterrows():
    #     player = Players(Name=row.Name, Pos=row.Pos, Age=row.Age)
    #     db.session.add(player)
    #     db.session.commit()

    # df = pd.read_csv('app/static/files/Team_Stats.csv')
    
    # for index, row in df.iterrows():
    #     team_stats = Team_Stats(
    #         TeamID=row.TeamID,
    #         Gms=row.Gms,
    #         MP=row.MP,
    #         FG=row.FG,
    #         FGA=row.FGA,
    #         FGP=row.FGP,
    #         ThreeP=row.ThreeP,
    #         ThreePA=row.ThreePA,
    #         ThreePP=row.ThreePP,
    #         TwoP=row.TwoP,
    #         TwoPA=row.TwoPA,
    #         TwoPP=row.TwoPP,
    #         FT=row.FT,
    #         FTA=row.FTA,
    #         FTP=row.FTP,
    #         ORB=row.ORB,
    #         DRB=row.DRB,
    #         TRB=row.TRB,
    #         AST=row.AST,
    #         STL=row.STL,
    #         BLK=row.BLK,
    #         TOV=row.TOV,
    #         PF=row.PF,
    #         PTS=row.PTS
    #     )
    #     db.session.add(team_stats)
    #     db.session.commit()

    # df = pd.read_csv('app/static/files/Top_Scorers.csv')
    # df = df.replace(np.nan, -1)
    # for index, row in df.iterrows():
    #     top_scorer = Top_Scorers(
    #         Points=row.Points,
    #         Name=row.Name,
    #         Year=row.Year,
    #         TeamName=row.TeamName,
    #         OppTeamName=row.OppTeamName,
    #         TeamScore=row.TeamScore,
    #         OppTeamScore=row.OppTeamScore,
    #         MinsPlayed=row.MinsPlayed
    #     )

    #     db.session.add(top_scorer)
    #     db.session.commit()

    return "Success! All data has been reset."