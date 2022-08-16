import json
from datetime import datetime

import psutil
from numpy import random
from psutil._common import bytes2human

from app import create_app
from app.database import db
from app.marshmallow import ma
from app.routes import create_routes

app, api = create_app()
app.config.update({
    "TESTING": True,
})
create_routes(api)

# ---------- GET TESTS ---------- #


def test_list_worker(app_test):
    response = app_test.test_client().get('/api/worker')
    response_json = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert isinstance(response_json, list)


def test_list_infos_by_worker(app_test):
    response = app_test.test_client().get('/api/infosystem/worker/1')
    response_json = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert isinstance(response_json, list)


# ---------- POST TESTS ---------- #

def test_post_worker(app_test):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data_post = {
        "name": f"worker_{str(random.randint(100))}",
    }
    response = app_test.test_client().post(f"/api/worker", headers=headers, json=data_post)
    response_json = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
    assert isinstance(response_json, dict)


def test_post_info(app_test):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data_post = {
        # boot_time,cpu_count,cpu_freq,cpu_stats,cpu_times,disk_partitions,
        # getloadavg,pids,swap_memory,virtual_memory
        "disk_available": psutil.disk_usage('/').percent,
        "using_ram": bytes2human(psutil.virtual_memory().used),
        "n_process": len(psutil.pids()),
        "created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "worker_id": random.randint(100),
    }
    response = app_test.test_client().post(f"/api/worker", headers=headers, json=data_post)
    response_json = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
    assert isinstance(response_json, dict)


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    test_list_worker(app)
    test_list_infos_by_worker(app)
    test_post_worker(app)
