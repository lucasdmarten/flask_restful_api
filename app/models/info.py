from datetime import datetime
from typing import List

import numpy as np
from pandas import to_datetime

from app.database import db


class InfoModel(db.Model):
    __tablename__ = "infosystem"

    id = db.Column(db.Integer, primary_key=True)
    disk_available = db.Column(
        db.Float(precision=2), nullable=False, default=np.random.randint(1, 6)
    )
    using_ram = db.Column(
        db.Float(precision=2), nullable=False, default=np.random.randint(0, 100)
    )
    n_process = db.Column(db.Integer, nullable=False, default=np.random.randint(1, 600))

    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    worker_id = db.Column(db.Integer, db.ForeignKey("worker.id"), nullable=False)

    def __init__(
        self, disk_available, using_ram, n_process, created,  worker_id
    ):
        # self.id = id
        self.disk_available = disk_available
        self.using_ram = using_ram
        self.n_process = n_process
        self.created = created
        self.worker_id = worker_id

    def __repr__(self):
        return "InfoModel(id_worker=%s)" % self.worker_id

    @classmethod
    def find_all(cls) -> List["InfoModel"]:
        return cls.query.all()

    @classmethod
    def find_by_worker_id(cls, _worker_id) -> List["InfoModel"]:
        return cls.query.filter_by(worker_id=_worker_id).all()

    @classmethod
    def find_by_period(cls, init, end) -> List["InfoModel"]:
        date_fmt = "%Y-%m-%dT%H:%M:%S"
        init, end = datetime.strptime(init, date_fmt), datetime.strptime(end, date_fmt)
        query = [
            data
            for data in cls.find_all()
            if (to_datetime(data.created) >= end)
            and (to_datetime(data.created) <= init)
        ]
        return query

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
