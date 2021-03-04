import os


def init_app(app):
    app.config["SECRET_KEY"] = "simple_api_test"

    app.config["MONGODB_SETTINGS"] = {
        "db": "simpleAPI",
        "host": "mongodb+srv://andrequeiroz:guilherme21@cluster0.wqki1.mongodb.net/simpleAPI?retryWrites=true&w=majority",
    }
