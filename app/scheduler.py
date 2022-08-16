from datetime import datetime

import flask_apscheduler as flask_scheduler
import requests
import psutil
from psutil._common import bytes2human
scheduler = flask_scheduler.APScheduler()

def post_infosystem(id_worker=6):
    url = "http://127.0.0.1:5000/api/infosystem/worker"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data_post = {
        # boot_time,cpu_count,cpu_freq,cpu_stats,cpu_times,disk_partitions,
        # getloadavg,pids,swap_memory,virtual_memory
        "disk_available": psutil.disk_usage('/').percent,
        "using_ram": bytes2human(psutil.virtual_memory().used),
        "n_process": len(psutil.pids()),
        "created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "worker_id": id_worker,
    }
    requests.post(f"{url}/{id_worker}", headers=headers, json=data_post)
