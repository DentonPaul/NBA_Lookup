from flask import Blueprint, render_template
import pandas as pd
from app.extensions import db

initialize_bp = Blueprint('initialize', __name__)

@initialize_bp.route('/initialize')
def index():
    
    sql = r"""
        USE `nba_dev`;
        DROP procedure IF EXISTS `GetTeamGeneral`;

        DELIMITER $$
        USE `nba_dev`$$
        CREATE PROCEDURE `GetTeamGeneral` (IN team_name varchar(500))
        BEGIN
        SELECT teamname, teamabbr, location from teams where teamname = team_name;
        END$$

        DELIMITER ;
    """

    db.session.execute(sql)
    db.session.commit()

    return "this endpoint does nothing"


# stored procedure code below

# USE `nba_dev`;
# DROP procedure IF EXISTS `GetTeamGeneral`;

# DELIMITER $$
# USE `nba_dev`$$
# CREATE PROCEDURE `GetTeamGeneral` (IN team_name varchar(500))
# BEGIN
# SELECT teamname, teamabbr, location from teams where teamname = team_name;
# END$$

# DELIMITER ;


# USE `nba_dev`;
# DROP procedure IF EXISTS `GetTeamStats`;

# DELIMITER $$
# USE `nba_dev`$$
# CREATE PROCEDURE `GetTeamStats` (IN team_name varchar(500))
# BEGIN
# select ts.gms, ts.mp, ts.fg, ts.fga, ts.fgp, ts.threep, 
#             ts.threepa, ts.threepp, ts.twop, ts.twopa, ts.twopp, ts.ft, 
#             ts.fta, ts.ftp, ts.orb, ts.drb, ts.trb, ts.ast, ts.stl, ts.blk, ts.tov, ts.pf, ts.pts
#             from teams as t join teamstats as ts on ts.teamid = t.teamid where t.teamname = team_name;
# END$$

# DELIMITER ;

# DROP INDEX playerstats_index ON playerstats;
# CREATE INDEX playerstats_index ON playerstats(player) USING BTREE;

# DROP INDEX coachstats_index ON coachstats;
# CREATE INDEX coachstats_index ON coachstats(name) USING BTREE;