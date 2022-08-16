from flask import Blueprint, Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)

    with app.app_context():

        blueprint = Blueprint("api", __name__, url_prefix="/api")
        api = Api(blueprint, doc="/doc", title="Flask restful owl")
        app.register_blueprint(blueprint=blueprint)
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/data.db"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["PROPAGATE_EXCEPTIONS"] = True

        return app, api
