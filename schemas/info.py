from models.info import InfoModel
from plugins.marshmallow import ma
from plugins.database import db


class InfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InfoModel
        load_instance = True
        load_only = ("infoz",)
        sqla_session = db.session
        include_fk = True
