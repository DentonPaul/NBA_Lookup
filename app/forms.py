from flask.scaffold import F
from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields.html5 import DecimalField
from wtforms.validators import DataRequired

from wtforms.validators import Length
from app.models import Teams
from app.extensions import db

class TeamForm(FlaskForm):
    TeamName = StringField('Team Name', validators=[Length(min=2, max=60), DataRequired()])

class PlayerLookupForm(FlaskForm):
    PlayerName = StringField('Player Name', validators=[Length(min=2, max=60), DataRequired()])

class PlayerAddForm(FlaskForm):
    PlayerName = StringField('Player Name', validators=[DataRequired(), Length(min=2, max=60)])
    team = StringField('Team', validators=[DataRequired(), Length(min=2, max=60)])
    pos = StringField('Position', validators=[DataRequired(), Length(min=1, max=60)])
    gms = DecimalField('Number of Games Played', validators=[DataRequired()])
    fga = DecimalField('FGA', validators=[DataRequired()])
    fg = DecimalField('FGM', validators=[DataRequired()])
    twopa = DecimalField('2PA', validators=[DataRequired()])
    twop = DecimalField('2PM', validators=[DataRequired()])
    threepa = DecimalField('3PA', validators=[DataRequired()])
    threep = DecimalField('3PM', validators=[DataRequired()])
    fta = DecimalField('FTA', validators=[DataRequired()])
    ft = DecimalField('FGM', validators=[DataRequired()])
    orb = DecimalField('Offensive Rebounds', validators=[DataRequired()])
    drb = DecimalField('Deffensive Rebounds', validators=[DataRequired()])
    ast = DecimalField('Assists', validators=[DataRequired()])
    blk = DecimalField('Blocks', validators=[DataRequired()])
    tov = DecimalField('Turnovers', validators=[DataRequired()])
    stl = DecimalField('Turnovers', validators=[DataRequired()])
    pf = DecimalField('Personal Fouls', validators=[DataRequired()])
    pts = DecimalField('Points', validators=[DataRequired()])
    age = DecimalField('Age', validators=[DataRequired()])

    # def validate(self):
    #     check_validate = super(PlayerAddForm, self).validate()
    #     if not check_validate:
    #         return False

    #     q = db.session.query(Teams.teamname.distinct().label('name'))
    #     team_names = [str(row.name) for row in q.all()]

    #     if str(self.team.data) not in team_names:
    #         return False
    #     return True