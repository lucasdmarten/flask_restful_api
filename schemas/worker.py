from models.worker import WorkerModel
from plugins.marshmallow import ma


class WorkerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkerModel
        load_instance = True
        #load_only = ("monitoring",)
        include_fk = True
