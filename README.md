# NBA Lookup App
- An online platform that makes it easy to explore team, player, and game data.

## Group Members
Denton Paul
Claudia Duncan
Colin Hayes
Peter Cunha

## Code that was ran on MySQL
```
USE `nba_dev`;
DROP procedure IF EXISTS `GetTeamGeneral`;

DELIMITER $$
USE `nba_dev`$$
CREATE PROCEDURE `GetTeamGeneral` (IN team_name varchar(500))
BEGIN
SELECT teamname, teamabbr, location from teams where teamname = team_name;
END$$

DELIMITER ;

USE `nba_dev`;
DROP procedure IF EXISTS `GetTeamStats`;

DELIMITER $$
USE `nba_dev`$$
CREATE PROCEDURE `GetTeamStats` (IN team_name varchar(500))
BEGIN
select ts.gms, ts.mp, ts.fg, ts.fga, ts.fgp, ts.threep, 
             ts.threepa, ts.threepp, ts.twop, ts.twopa, ts.twopp, ts.ft, 
             ts.fta, ts.ftp, ts.orb, ts.drb, ts.trb, ts.ast, ts.stl, ts.blk, ts.tov, ts.pf, ts.pts
             from teams as t join teamstats as ts on ts.teamid = t.teamid where t.teamname = team_name;
END$$

DELIMITER ;


DROP INDEX playerstats_index ON playerstats;
CREATE INDEX playerstats_index ON playerstats(player) USING BTREE;

DROP INDEX player_index ON players;
CREATE INDEX player_index ON players(name);

DROP INDEX coachstats_index ON coachstats;
CREATE INDEX coachstats_index ON coachstats(name) USING BTREE;
```

#### Helpful Commands
- export DYLD_LIBRARY_PATH="/usr/local/mysql/lib:$PATH"
- FLASK_ENV=development FLASK_APP="app:create_app" flask shell