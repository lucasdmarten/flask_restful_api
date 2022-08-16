import json

from app import create_app
from app.database import db
from app.marshmallow import ma
from app.routes import create_routes

app, api = create_app()
app.config.update({
    "TESTING": True,
})
create_routes(api_test)


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


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    test_list_worker(app)
    test_list_infos_by_worker(app)

