"""Joel's Flask app."""

from flask import Flask, url_for, redirect
from flaskplay.treats import treats_blueprint
from .extensions import shelve


def create_app(config_object_name):
    """Create overall application object, given a configuration object name."""

    app = Flask(__name__)
    app.config.from_object(config_object_name)

    shelve.init_app(app)

    app.register_blueprint(treats_blueprint, url_prefix="/treats")

    @app.route("/")
    def homepage():
        """Main homepage; redirect to treats app."""

        return redirect(url_for("treats.index"))

    return app
