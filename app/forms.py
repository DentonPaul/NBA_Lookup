from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields.html5 import DecimalField

from wtforms.validators import Length

class TeamForm(FlaskForm):
    TeamName = StringField('Team Name', [Length(min=2, max=60)])