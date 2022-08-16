from flask import jsonify
from marshmallow import ValidationError

from app import create_app
from app.database import db
from app.marshmallow import ma
from app.routes import create_routes
from app.scheduler import scheduler, post_infosystem

app, api = create_app()
create_routes(api)


# noinspection PyDeprecation
@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    #scheduler.add_job(
    #    id='Scheduled Task', func=post_infosystem,
    #    trigger="interval", seconds=10
    #)
    #scheduler.start()
    app.run(port=5000, debug=True)
