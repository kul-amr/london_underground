from flask_restplus import Api
from flask import Blueprint

from .main.controller.station_controller import api as station_namespace



blueprint = Blueprint('api',__name__)

api = Api(blueprint,
          title='london underground api',
          version='1.0',
          description='london underground api desc')


api.add_namespace(station_namespace,path='/station')