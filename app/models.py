from typing import NamedTuple
from sqlalchemy.orm import validates
from app.extensions import db

class Coach_Stats(db.Model):
    __tablename__ = 'coachstats'
    name = db.Column(db.String(255), primary_key = True)
    team = db.Column(db.String(255), nullable = False)
    seasg = db.Column(db.Integer, nullable = False)
    seasw = db.Column(db.Integer, nullable = False)
    seasl = db.Column(db.Integer, nullable = False)
    frang = db.Column(db.Integer, nullable = False)
    franw = db.Column(db.Integer, nullable = False)
    franl = db.Column(db.Integer, nullable = False)
    carew = db.Column(db.Integer, nullable = False)
    carel = db.Column(db.Integer, nullable = False)
    carewp = db.Column(db.Float, nullable = False)
    poseasg = db.Column(db.Integer, nullable = True)
    poseasw = db.Column(db.Integer, nullable = True)
    poseasl = db.Column(db.Integer, nullable = True)
    pofrang = db.Column(db.Integer, nullable = True)
    pofranw = db.Column(db.Integer, nullable = True)
    pofranl = db.Column(db.Integer, nullable = True)
    pocareg = db.Column(db.Integer, nullable = True)
    pocarew = db.Column(db.Integer, nullable = True)
    pocarel = db.Column(db.Integer, nullable = True)


class Coaches(db.Model):
    __tablename__ = 'coaches'
    name = db.Column(db.String(225), primary_key = True)
    teamid = db.Column(db.Integer, nullable = False)

class Player_Stats(db.Model):
    __tablename__ = 'playerstats'
    player = db.Column(db.String(225), primary_key = True)
    tm = db.Column(db.String(225), primary_key = True)
    gms = db.Column(db.Integer, nullable = False)
    gstart = db.Column(db.Integer, nullable = False)
    mp = db.Column(db.Integer, nullable = False)
    fg = db.Column(db.Integer, nullable = False)
    fga = db.Column(db.Integer, nullable = False)
    fgp = db.Column(db.Float, nullable = False)
    threep = db.Column(db.Integer, nullable = False)
    threepa = db.Column(db.Integer, nullable = False)
    threepp = db.Column(db.Float, nullable = False)
    twop = db.Column(db.Integer, nullable = False)
    twopa = db.Column(db.Integer, nullable = False)
    twopp = db.Column(db.Float, nullable = False)
    efgp = db.Column(db.Float, nullable = False)
    ft = db.Column(db.Integer, nullable = False)
    fta = db.Column(db.Integer, nullable = False)
    ftp = db.Column(db.Float, nullable = False)
    orb = db.Column(db.Integer, nullable = False)
    drb = db.Column(db.Integer, nullable = False)
    trb = db.Column(db.Integer, nullable = False)
    ast = db.Column(db.Integer, nullable = False)
    stl = db.Column(db.Integer, nullable = False)
    blk = db.Column(db.Integer, nullable = False)
    tov = db.Column(db.Integer, nullable = False)
    pf = db.Column(db.Integer, nullable = False)
    pts = db.Column(db.Integer, nullable = False)

class Players(db.Model):
    __tablename__ = 'players'
    name = db.Column(db.String(225), primary_key = True)
    pos = db.Column(db.String(225), nullable = False)
    age = db.Column(db.Integer, nullable = False)

class Team_Stats(db.Model):
    __tablename__ = 'teamstats'
    teamid = db.Column(db.Integer, primary_key = True)
    gms = db.Column(db.Integer, nullable = False)
    mp = db.Column(db.Integer, nullable = False)
    fg = db.Column(db.Integer, nullable = False)
    fga = db.Column(db.Integer, nullable = False)
    fgp = db.Column(db.Float, nullable = False)
    threep = db.Column(db.Integer, nullable = False)
    threepa = db.Column(db.Integer, nullable = False)
    threepp = db.Column(db.Float, nullable = False)
    twop = db.Column(db.Integer, nullable = False)
    twopa = db.Column(db.Integer, nullable = False)
    twopp = db.Column(db.Float, nullable = False)
    ft = db.Column(db.Integer, nullable = False)
    fta = db.Column(db.Integer, nullable = False)
    ftp = db.Column(db.Float, nullable = False)
    orb = db.Column(db.Integer, nullable = False)
    drb = db.Column(db.Integer, nullable = False)
    trb = db.Column(db.Integer, nullable = False)
    ast = db.Column(db.Integer, nullable = False)
    stl = db.Column(db.Integer, nullable = False)
    blk = db.Column(db.Integer, nullable = False)
    tov = db.Column(db.Integer, nullable = False)
    pf = db.Column(db.Integer, nullable = False)
    pts = db.Column(db.Integer, nullable = False)


class Teams(db.Model):
    __tablename__ = 'teams'
    # __table_args__ = {"schema": "teams"}
    teamid = db.Column(db.Integer, primary_key = True)
    teamname = db.Column(db.String(225), nullable = False)
    teamabbr = db.Column(db.String(225), nullable = False)
    location = db.Column(db.String(225), nullable = False)

class Top_Scorers(db.Model):
    __tablename__ = 'topscorers'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    points = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(225), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    teamname = db.Column(db.String(225), nullable = False)
    oppteamname = db.Column(db.String(225), nullable = False)
    teamscore = db.Column(db.Integer, nullable = False)
    oppteamscore = db.Column(db.Integer, nullable = False)
    minsplayed = db.Column(db.Integer, nullable = True)