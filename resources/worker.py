from flask import request

from flask_restx import Namespace, Resource, fields
from models.worker import WorkerModel
from schemas.worker import WorkerSchema


WORKER_NOT_FOUND = "Worker not found."
WORKER_ALREADY_EXISTS = "Worker '{}' Already exists."

worker_ns = Namespace("worker", description="Worker related operations")
workers_ns = Namespace("workers", description="Workers related operations")

worker_schema = WorkerSchema()
worker_list_schema = WorkerSchema(many=True)

# Model required by flask_restx for expect
store = worker_ns.model("Worker", {"name": fields.String("Name of the Worker")})



class WorkerList(Resource):
    @workers_ns.doc("Get all the Workers")
    def get(self):
        return worker_list_schema.dump(WorkerModel.find_all()), 200

    @workers_ns.expect(store)
    @workers_ns.doc("Create a Worker")
    def post(self):
        store_json = request.get_json()
        name = store_json["name"]
        if WorkerModel.find_by_name(name):
            return {"message": WORKER_ALREADY_EXISTS.format(name)}, 400

        store_data = worker_schema.load(store_json)
        store_data.save_to_db()

        return worker_schema.dump(store_data), 201
