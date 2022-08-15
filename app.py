from flask import Blueprint, Flask, jsonify

from flask_restx import Api
from marshmallow import ValidationError
from plugins.database import db
from plugins.marshmallow import ma
from resources.info import ListInfoWorker, ByDateInfoWorker, InfoList, infos_ns, worker_info, worker_by_date_info
from resources.worker import WorkerList, worker_ns, workers_ns


app = Flask(__name__)

blueprint = Blueprint("api", __name__, url_prefix="/api")

api = Api(blueprint, doc="/doc", title="Sample Flask-RestX Application")

app.register_blueprint(blueprint=blueprint)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

api.add_namespace(worker_info)
api.add_namespace(infos_ns)
api.add_namespace(worker_ns)
api.add_namespace(workers_ns)
api.add_namespace(worker_by_date_info)


# noinspection PyDeprecation
@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


#--------------- # test # --------------------
#worker_info.add_resource(List2InfoWorker, "")
#---------------------------------------------

worker_by_date_info.add_resource(ByDateInfoWorker, "/<init>/<end>")
worker_info.add_resource(ListInfoWorker, "/<int:worker_id>")
workers_ns.add_resource(WorkerList, "")
infos_ns.add_resource(InfoList, "")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
