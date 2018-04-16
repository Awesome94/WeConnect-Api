import os
from flask import Flask

from app.v1.businesses import views
from app.v1.users import views
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    return app