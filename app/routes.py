from app.resources.info import InfoList, infosystem_endpoints
from app.resources.worker import WorkerList, worker_endpoint


def create_routes(api):
    # ------------- filter data by worker id ------------- #
    api.add_namespace(infosystem_endpoints)
    infosystem_endpoints.add_resource(InfoList, "/worker/<int:worker_id>")

    # ------------- list workers ------------- #
    api.add_namespace(worker_endpoint)
    worker_endpoint.add_resource(WorkerList, "")
