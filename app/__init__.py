from flask import Flask, render_template

from app.blueprints.landing import landing_bp
from app.blueprints.players import players_bp
from app.blueprints.trades import trades_bp
from app.blueprints.drafted import drafted_bp
from app.blueprints.retired import retired_bp
from app.blueprints.teams import teams_bp
from app.blueprints.reset_data import reset_data_bp
from app.blueprints.data import see_data_bp

from app.config import configurations

from webassets.loaders import PythonLoader as PythonAssetsLoader
from app import assets

from app.extensions import assets_env, db

def create_app(env_name='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[env_name])

    db.init_app(app)
    assets_env.init_app(app)

    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register blueprints
    app.register_blueprint(landing_bp)
    app.register_blueprint(players_bp)
    app.register_blueprint(trades_bp)
    app.register_blueprint(teams_bp)
    app.register_blueprint(drafted_bp)
    app.register_blueprint(retired_bp)
    app.register_blueprint(reset_data_bp)
    app.register_blueprint(see_data_bp)

    # register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500

    return app