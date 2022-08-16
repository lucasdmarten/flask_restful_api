from flask import request
from flask_restx import Namespace, Resource, fields

from app.models.info import InfoModel
from app.models.worker import WorkerModel
from app.schemas.info import InfoSchema

INFO_NOT_FOUND = "Info not found."
INFO_ALREADY_EXISTS = "Info '{}' Already exists."

infosystem_endpoints = Namespace("infosystem", description="infos related operations")

info_schema = InfoSchema()
infos_list_schema = InfoSchema(many=True)

# Model required by flask_restx for expect
store = infosystem_endpoints.model(
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


class InfoList(Resource):
    @staticmethod
    @infosystem_endpoints.doc("Get all the Infos")
    def get(worker_id):
        data_object = InfoModel.find_by_worker_id(worker_id)
        return infos_list_schema.dump(data_object), 200

    @staticmethod
    @infosystem_endpoints.expect(store)
    @infosystem_endpoints.doc("Create a Info")
    def post(worker_id):
        store_json = request.get_json()

        if not WorkerModel.find_by_id(store_json["worker_id"]):
            return {"message": "failed"}

        store_data = info_schema.load(store_json)
        store_data.save_to_db()

        return info_schema.dump(store_data), 201
