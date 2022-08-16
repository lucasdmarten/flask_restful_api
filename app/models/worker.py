from typing import List

from app.database import db
from app.models.info import InfoModel


class WorkerModel(db.Model):
    __tablename__ = "worker"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    infoz = db.relationship(InfoModel, backref="info", lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "WorkModel(name=%s)" % self.name

    @classmethod
    def find_by_name(cls, name) -> List["WorkerModel"]:
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> List["WorkerModel"]:
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["WorkerModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
