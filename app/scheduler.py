from flask_apscheduler import APScheduler
import requests
from numpy import random
from datetime import datetime


scheduler = APScheduler()


def post_infosystem(id_worker=6):
    url = "http://127.0.0.1:5000/api/infosystem/worker"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data_post = {
        "disk_available": random.randint(100),
        "using_ram": random.randint(100),
        "n_process": random.randint(1000),
        "created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "updated": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "worker_id": id_worker
    }
    requests.post(
        f"{url}/{id_worker}", headers=headers, json=data_post
    )
