from flask import request

from flask_restx import Namespace, Resource, fields
from models.info import InfoModel
from models.worker import WorkerModel
from schemas.info import InfoSchema

from datetime import datetime, timedelta

INFO_NOT_FOUND = "Info not found."
INFO_ALREADY_EXISTS = "Info '{}' Already exists."

infos_ns = Namespace("infos", description="infos related operations")
worker_info = Namespace("worker", description="worker info related operations")
worker_by_date_info = Namespace("by_date", description="worker info related operations")

info_schema = InfoSchema()
infos_list_schema = InfoSchema(many=True)

# Model required by flask_restx for expect
store = infos_ns.model(
    "Info",
    {
        "disk_available": fields.Float("disk_available"),
        "using_ram": fields.Float("using_ram"),
        "n_process": fields.Integer("n_process"),
        "created": fields.DateTime("created"),
        "updated": fields.DateTime("updated"),
        "worker_id": fields.Integer("worker_id"),
    },
)


class ListInfoWorker(Resource):
    @staticmethod
    def get(worker_id):
        return infos_list_schema.dump(InfoModel.find_by_worker_id(worker_id)), 200


class ByDateInfoWorker(Resource):
    @staticmethod
    def get(init, end):
        data_query = InfoModel.find_by_period(init, end)
        return infos_list_schema.dump(data_query), 200


class InfoList(Resource):
    @infos_ns.doc("Get all the Infos")
    def get(self):
        return infos_list_schema.dump(InfoModel.find_all()), 200

    @infos_ns.expect(store)
    @infos_ns.doc("Create a Info")
    def post(self):
        store_json = request.get_json()

        if not WorkerModel.find_by_id(store_json["worker_id"]):
            return {"message": "failed"}

        store_data = info_schema.load(store_json)
        store_data.save_to_db()

        return info_schema.dump(store_data), 201
