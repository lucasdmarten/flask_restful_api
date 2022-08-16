import os, sys
import requests
import json
from numpy import random
from datetime import datetime
import matplotlib.pyplot as plt


url_name = "http://127.0.0.1:5000/api"

json_headers = {"Content-Type": "application/json; charset=utf-8"}


# ------------- ACTIONS INFOSYSTEM ------------- #

def post_infos(url, headers, id_worker):
	data_post = {
		"disk_available": random.randint(100),
		"using_ram": random.randint(100),
		"n_process": random.randint(1000),
		"created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
		"worker_id": int(id_worker)
	}
	print('tst')
	print(f"{url}/infosystem/worker/{id_worker}")
	response = requests.post(
		f"{url}/infosystem/worker/{id_worker}",
		headers=headers, json=data_post
	)
	print(response)
	print("Status Code", response.status_code)
	print("JSON Response ", response.json())
	return response.json()


def get_infos(url, headers, id_worker):

	response = requests.get(f"{url}/infosystem/worker/{id_worker}", headers=headers)

	print("Status Code", response.status_code)
	print("JSON Response ", response.json())
	return response.json()


# ------------- ACTIONS WORKERS ------------- #

def post_workers(url, headers, name_worker):
	data_post = {
		"name": name_worker,
	}
	response = requests.post(f"{url}/worker", headers=headers, json=data_post)

	print("Status Code", response.status_code)
	print("JSON Response ", response.json())


def get_workers(url, headers):
	print(f"{url}/workers")
	response = requests.get(f"{url}/worker", headers=headers)

	print("Status Code", response.status_code)
	print("JSON Response ", response.json())


# ------------- RUN TESTS ------------- #


if sys.argv[1] == "workers":
	if sys.argv[2] == "GET": get_workers(url_name, json_headers)
	if sys.argv[2] == "POST": post_workers(url_name, json_headers, sys.argv[3])

if sys.argv[1] == "infos":
	if sys.argv[2] == "GET": data = get_infos(url_name, json_headers, sys.argv[3])
	if sys.argv[2] == "POST": data = post_infos(url_name, json_headers, sys.argv[3])

#def null_block():
#if data:

	#disk_available = [data_store['disk_available'] for data_store in data]
	#n_process = [data_store['n_process'] for data_store in data]
	#worker_id = [data_store['worker_id'] for data_store in data]
	#updated = [data_store['updated'] for data_store in data]
	#using_ram = [data_store['using_ram'] for data_store in data]
	#created = [data_store['created'] for data_store in data]
	#plt.figure(figsize=(20,20))
	#plt.plot(created, disk_available)
	#plt.xticks(rotation=90)
	#plt.show()
