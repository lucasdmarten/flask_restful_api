from app.database import db
from app.marshmallow import ma
from app.models.worker import WorkerModel


class WorkerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkerModel
        load_instance = True
        load_only = ("infoz",)
        sqla_session = db.session
        include_fk = True
