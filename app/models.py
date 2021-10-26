from typing import NamedTuple
from sqlalchemy.orm import validates
from app.extensions import db

class Coach_Stats(db.Model):
    __tablename__ = 'Coach_Stats'
    Name = db.Column(db.String(255), primary_key = True)
    Team = db.Column(db.String(255), nullable = False)
    SeasG = db.Column(db.Integer, nullable = False)
    SeasW = db.Column(db.Integer, nullable = False)
    SeasL = db.Column(db.Integer, nullable = False)
    FranG = db.Column(db.Integer, nullable = False)
    FranW = db.Column(db.Integer, nullable = False)
    FranL = db.Column(db.Integer, nullable = False)
    CareW = db.Column(db.Integer, nullable = False)
    CareL = db.Column(db.Integer, nullable = False)
    CareWP = db.Column(db.Float, nullable = False)
    POSeasG = db.Column(db.Integer, nullable = True)
    POSeasW = db.Column(db.Integer, nullable = True)
    POSeasL = db.Column(db.Integer, nullable = True)
    POFranG = db.Column(db.Integer, nullable = True)
    POFranW = db.Column(db.Integer, nullable = True)
    POFranL = db.Column(db.Integer, nullable = True)
    POCareG = db.Column(db.Integer, nullable = True)
    POCareW = db.Column(db.Integer, nullable = True)
    POCareL = db.Column(db.Integer, nullable = True)


class Coaches(db.Model):
    __tablename__ = 'Coaches'
    Name = db.Column(db.String(225), primary_key = True)
    TeamID = db.Column(db.Integer, nullable = False)

class Player_Stats(db.Model):
    __tablename__ = 'Player_Stats'
    Player = db.Column(db.String(225), primary_key = True)
    Tm = db.Column(db.String(225), primary_key = True)
    Gms = db.Column(db.Integer, nullable = False)
    Gstart = db.Column(db.Integer, nullable = False)
    MP = db.Column(db.Integer, nullable = False)
    FG = db.Column(db.Integer, nullable = False)
    FGA = db.Column(db.Integer, nullable = False)
    FGP = db.Column(db.Float, nullable = False)
    ThreeP = db.Column(db.Integer, nullable = False)
    ThreePA = db.Column(db.Integer, nullable = False)
    ThreePP = db.Column(db.Float, nullable = False)
    TwoP = db.Column(db.Integer, nullable = False)
    TwoPA = db.Column(db.Integer, nullable = False)
    TwoPP = db.Column(db.Float, nullable = False)
    eFGP = db.Column(db.Float, nullable = False)
    FT = db.Column(db.Integer, nullable = False)
    FTA = db.Column(db.Integer, nullable = False)
    FTP = db.Column(db.Float, nullable = False)
    ORB = db.Column(db.Integer, nullable = False)
    DRB = db.Column(db.Integer, nullable = False)
    TRB = db.Column(db.Integer, nullable = False)
    AST = db.Column(db.Integer, nullable = False)
    STL = db.Column(db.Integer, nullable = False)
    BLK = db.Column(db.Integer, nullable = False)
    TOV = db.Column(db.Integer, nullable = False)
    PF = db.Column(db.Integer, nullable = False)
    PTS = db.Column(db.Integer, nullable = False)

class Players(db.Model):
    __tablename__ = 'Players'
    Name = db.Column(db.String(225), primary_key = True)
    Pos = db.Column(db.String(225), nullable = False)
    Age = db.Column(db.Integer, nullable = False)

class Team_Stats(db.Model):
    __tablename__ = 'Team_Stats'
    TeamID = db.Column(db.Integer, primary_key = True)
    Gms = db.Column(db.Integer, nullable = False)
    MP = db.Column(db.Integer, nullable = False)
    FG = db.Column(db.Integer, nullable = False)
    FGA = db.Column(db.Integer, nullable = False)
    FGP = db.Column(db.Float, nullable = False)
    ThreeP = db.Column(db.Integer, nullable = False)
    ThreePA = db.Column(db.Integer, nullable = False)
    ThreePP = db.Column(db.Float, nullable = False)
    TwoP = db.Column(db.Integer, nullable = False)
    TwoPA = db.Column(db.Integer, nullable = False)
    TwoPP = db.Column(db.Float, nullable = False)
    FT = db.Column(db.Integer, nullable = False)
    FTA = db.Column(db.Integer, nullable = False)
    FTP = db.Column(db.Float, nullable = False)
    ORB = db.Column(db.Integer, nullable = False)
    DRB = db.Column(db.Integer, nullable = False)
    TRB = db.Column(db.Integer, nullable = False)
    AST = db.Column(db.Integer, nullable = False)
    STL = db.Column(db.Integer, nullable = False)
    BLK = db.Column(db.Integer, nullable = False)
    TOV = db.Column(db.Integer, nullable = False)
    PF = db.Column(db.Integer, nullable = False)
    PTS = db.Column(db.Integer, nullable = False)


class Teams(db.Model):
    __tablename__ = 'Teams'
    __table_args__ = {"schema": "Teams"}
    TeamID = db.Column(db.Integer, primary_key = True)
    TeamName = db.Column(db.String(225), nullable = False)
    TeamAbbr = db.Column(db.String(225), nullable = False)
    Location = db.Column(db.String(225), nullable = False)

class Top_Scorers(db.Model):
    __tablename__ = 'Top_Scorers'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    Points = db.Column(db.Integer, nullable = False)
    Name = db.Column(db.String(225), nullable = False)
    Year = db.Column(db.Integer, nullable = False)
    TeamName = db.Column(db.String(225), nullable = False)
    OppTeamName = db.Column(db.String(225), nullable = False)
    TeamScore = db.Column(db.Integer, nullable = False)
    OppTeamScore = db.Column(db.Integer, nullable = False)
    MinsPlayed = db.Column(db.Integer, nullable = True)