from flask import Blueprint, render_template
from app.forms import PlayerRetired
from app.models import Player_Stats, Players
from app.extensions import db

retired_bp = Blueprint('retired', __name__)

@retired_bp.route('/retired')
def index():
    form = PlayerRetired()

    return render_template('retired/index.html', form=form)

@retired_bp.route('/retired/create', methods=['GET', 'POST'])
def create():
    form = PlayerRetired()

    #####
    # ORM
    #####
    Players.query.filter_by(name=form.PlayerName.data).delete()
    Player_Stats.query.filter_by(player=form.PlayerName.data).delete()
    db.session.commit()

    message = f"Success! {form.PlayerName.data} has been deleted from our database."
    return render_template('retired/index.html', form=form, message=message)