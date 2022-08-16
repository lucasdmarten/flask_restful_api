from app.database import db
from app.marshmallow import ma
from app.models.info import InfoModel


class InfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InfoModel
        load_instance = True
        load_only = ("infoz",)
        sqla_session = db.session
        include_fk = True
