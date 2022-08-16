from flask import request
from flask_restx import Namespace, Resource, fields

from app.models.worker import WorkerModel
from app.schemas.worker import WorkerSchema

WORKER_NOT_FOUND = "Worker not found."
WORKER_ALREADY_EXISTS = "Worker '{}' Already exists."

worker_endpoint = Namespace("worker", description="worker info related operations")

worker_schema = WorkerSchema()
worker_list_schema = WorkerSchema(many=True)

# Model required by flask_restx for expect
store = worker_endpoint.model("Worker", {"name": fields.String("Name of the Worker")})


class WorkerList(Resource):
    @staticmethod
    @worker_endpoint.doc("Get all the Workers")
    def get():
        return worker_list_schema.dump(WorkerModel.find_all()), 200

    @staticmethod
    @worker_endpoint.expect(store)
    @worker_endpoint.doc("Create a Worker")
    def post():
        store_json = request.get_json()
        name = store_json["name"]
        if WorkerModel.find_by_name(name):
            return {"message": WORKER_ALREADY_EXISTS.format(name)}, 400

        store_data = worker_schema.load(store_json)
        store_data.save_to_db()

        return worker_schema.dump(store_data), 201
