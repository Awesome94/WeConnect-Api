import os
from flask import Flask

from app.v1 import views

app = Flask(__name__)

# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(config[config_name])
#     config[config_name].init_app(app)

#     return app
