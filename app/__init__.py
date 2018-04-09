import os
from flask import Flask

app = Flask(__name__)

from app.v1.businesses import views
from app.v1.users import views
#app.config.from_object('config')
