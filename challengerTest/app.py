from flask import Flask
from flask_restful import Api
from database import db
import os
from model import model_task, model_user
from error.errors import errors

app = Flask(__name__)

environment_configuration = os.environ["CONFIGURATION_SETUP"]
app.config.from_object(environment_configuration)

if app.config["ENV"] == "development":
    app.config["MONGODB_SETTINGS"] = {
        "db": "simpleAPI",
        "host": "mongodb+srv://andrequeiroz:guilherme21@cluster0.wqki1.mongodb.net/simpleAPI?retryWrites=true&w=majority",
    }
else:
    app.config["MONGODB_SETTINGS"] = {
        "db": "simple-api-test",
        "host": "mongodb+srv://andrequeiroz:guilherme21@cluster0.dplrn.mongodb.net/simple-api-test?retryWrites=true&w=majority",
    }

api = Api(app, errors=errors)
db.init_app(app)

from route.route_user import init_routes_user
from route.route_task import init_routes_task

init_routes_user(api)
init_routes_task(api)

if __name__ == "__main__":
    app.run()
